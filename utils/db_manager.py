import psycopg2
from psycopg2 import pool
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import os
import json
import pytz

class DatabaseManager:
    """Handle PostgreSQL database operations for store monitoring"""

    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL')
        if not self.database_url:
            raise ValueError(
                "DATABASE_URL environment variable is not set. "
                "Please ensure PostgreSQL database is configured."
            )

        # Create connection pool for better performance
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            1,  # minconn
            10,  # maxconn
            self.database_url
        )

        self.init_database()

    def get_connection(self):
        """Get a database connection from pool"""
        return self.connection_pool.getconn()

    def return_connection(self, conn):
        """Return connection to pool"""
        self.connection_pool.putconn(conn)

    def init_database(self):
        """Initialize database tables"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            # Create stores table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS stores (
                    id SERIAL PRIMARY KEY,
                    url TEXT UNIQUE NOT NULL,
                    status TEXT NOT NULL DEFAULT 'UNCHECKED',
                    first_check TIMESTAMP WITH TIME ZONE,
                    last_check TIMESTAMP WITH TIME ZONE,
                    first_dead_date TIMESTAMP WITH TIME ZONE,
                    check_count INTEGER DEFAULT 0,
                    timezone_checked VARCHAR(100),
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Create check_history table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS check_history (
                    id SERIAL PRIMARY KEY,
                    store_id INTEGER REFERENCES stores(id) ON DELETE CASCADE,
                    status TEXT NOT NULL,
                    checked_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    response_time FLOAT,
                    status_code INTEGER
                )
            ''')

            # Create index for faster queries
            cur.execute('''
                CREATE INDEX IF NOT EXISTS idx_stores_status ON stores(status)
            ''')
            cur.execute('''
                CREATE INDEX IF NOT EXISTS idx_stores_url ON stores(url)
            ''')
            cur.execute('''
                CREATE INDEX IF NOT EXISTS idx_check_history_store_id ON check_history(store_id)
            ''')
            cur.execute('''
                CREATE INDEX IF NOT EXISTS idx_check_history_checked_at ON check_history(checked_at)
            ''')

            conn.commit()
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def load_urls(self, urls: List[str]) -> None:
        """Load new URLs into the database (optimized bulk insert)"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            # Prepare data for bulk insert
            clean_urls = [(url.strip(),) for url in urls if url.strip()]

            if clean_urls:
                # Use execute_values for bulk insert (much faster)
                from psycopg2.extras import execute_values

                execute_values(
                    cur,
                    '''
                    INSERT INTO stores (url, status, check_count)
                    VALUES %s
                    ON CONFLICT (url) DO NOTHING
                    ''',
                    clean_urls,
                    template="(%s, 'UNCHECKED', 0)"
                )

            conn.commit()
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_timezone(self):
        """Get Pacific timezone (Oregon)"""
        return pytz.timezone('America/Los_Angeles')

    def get_current_time(self):
        """Get current time in Pacific timezone (Oregon)"""
        # Get UTC time directly from system, then convert to Pacific
        from datetime import datetime as dt
        utc_now = dt.utcnow().replace(tzinfo=pytz.UTC)
        pacific_tz = self.get_timezone()
        return utc_now.astimezone(pacific_tz)

    def update_store_status(self, url: str, status: str, timezone_checked: str = None, response_time: float = None, status_code: int = None) -> None:
        """Update store status with timestamp and history tracking"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            # Get current time in Pacific timezone
            current_time = self.get_current_time()

            # Get previous status
            cur.execute('SELECT status FROM stores WHERE url = %s', (url,))
            result = cur.fetchone()
            previous_status = result[0] if result else None

            # Update store
            cur.execute('''
                UPDATE stores
                SET status = %s,
                    last_check = %s,
                    check_count = check_count + 1,
                    updated_at = %s,
                    timezone_checked = %s,
                    first_check = COALESCE(first_check, %s),
                    first_dead_date = CASE
                        WHEN %s = 'DEAD' AND %s != 'DEAD' THEN %s
                        WHEN %s != 'DEAD' AND %s = 'DEAD' THEN NULL
                        ELSE first_dead_date
                    END
                WHERE url = %s
            ''', (status, current_time, current_time, timezone_checked, current_time,
                  status, previous_status, current_time,
                  status, previous_status, url))

            # If the store didn't exist, insert it
            if not result:
                cur.execute('''
                    INSERT INTO stores (url, status, first_check, last_check, check_count, timezone_checked, first_dead_date)
                    VALUES (%s, %s, %s, %s, 1, %s, %s)
                ''', (url, status, current_time, current_time, timezone_checked,
                      current_time if status == 'DEAD' else None))


            # Add to history
            cur.execute('''
                INSERT INTO check_history (store_id, status, checked_at, response_time, status_code)
                VALUES ((SELECT id FROM stores WHERE url = %s), %s, %s, %s, %s)
            ''', (url, status, current_time, response_time, status_code))

            conn.commit()
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_data(self) -> Dict[str, Dict[str, Any]]:
        """Get all stores data"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            cur.execute('''
                SELECT url, status, first_check, last_check, first_dead_date, check_count, timezone_checked
                FROM stores
                ORDER BY url
            ''')

            data = {}
            for row in cur.fetchall():
                url, status, first_check, last_check, first_dead_date, check_count, timezone_checked = row
                data[url] = {
                    'status': status,
                    'first_check': first_check.isoformat() if first_check else None,
                    'last_check': last_check.isoformat() if last_check else None,
                    'first_dead_date': first_dead_date.isoformat() if first_dead_date else None,
                    'check_count': check_count,
                    'timezone_checked': timezone_checked
                }

            return data
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_stores_by_status(self, status: str) -> List[str]:
        """Get list of URLs with specific status"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            cur.execute('SELECT url FROM stores WHERE status = %s ORDER BY url', (status,))
            return [row[0] for row in cur.fetchall()]
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_status_counts(self) -> Dict[str, int]:
        """Get count of stores by status"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            cur.execute('''
                SELECT status, COUNT(*) as count
                FROM stores
                GROUP BY status
            ''')

            counts = {}
            for status, count in cur.fetchall():
                counts[status] = count

            return counts
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_total_count(self) -> int:
        """Get total number of stores"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            cur.execute('SELECT COUNT(*) FROM stores')
            return cur.fetchone()[0]
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_live_count(self) -> int:
        """Get number of LIVE stores"""
        return len(self.get_stores_by_status('LIVE'))

    def get_dead_count(self) -> int:
        """Get number of DEAD stores"""
        return len(self.get_stores_by_status('DEAD'))

    def get_unpaid_count(self) -> int:
        """Get number of UNPAID stores"""
        return len(self.get_stores_by_status('UNPAID'))

    def get_filtered_data(self, status_filters: List[str], search_term: str = "") -> Dict[str, Dict[str, Any]]:
        """Get filtered data based on status and search term"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            query = '''
                SELECT url, status, first_check, last_check, first_dead_date, check_count, timezone_checked
                FROM stores
                WHERE status = ANY(%s)
            '''
            params = [status_filters]

            if search_term:
                query += ' AND url ILIKE %s'
                params.append(f'%{search_term}%')

            query += ' ORDER BY url'

            cur.execute(query, params)

            filtered = {}
            for row in cur.fetchall():
                url, status, first_check, last_check, first_dead_date, check_count, timezone_checked = row
                filtered[url] = {
                    'status': status,
                    'first_check': first_check.isoformat() if first_check else None,
                    'last_check': last_check.isoformat() if last_check else None,
                    'first_dead_date': first_dead_date.isoformat() if first_dead_date else None,
                    'check_count': check_count,
                    'timezone_checked': timezone_checked
                }

            return filtered
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_timeline_data(self, days: int = None) -> List[Dict[str, Any]]:
        """Get timeline data for charts with optional date filtering"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            if days:
                # Filter by date range at database level
                cur.execute('''
                    SELECT
                        DATE(checked_at AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles') as check_date,
                        status,
                        COUNT(*) as count
                    FROM check_history
                    WHERE checked_at >= CURRENT_TIMESTAMP - INTERVAL '%s days'
                    GROUP BY DATE(checked_at AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles'), status
                    ORDER BY check_date, status
                ''', (days,))
            else:
                # Get all timeline data
                cur.execute('''
                    SELECT
                        DATE(checked_at AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles') as check_date,
                        status,
                        COUNT(*) as count
                    FROM check_history
                    GROUP BY DATE(checked_at AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles'), status
                    ORDER BY check_date, status
                ''')

            timeline_list = []
            for check_date, status, count in cur.fetchall():
                timeline_list.append({
                    'date': check_date.isoformat(),
                    'status': status,
                    'count': count
                })

            return timeline_list
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_dead_stores_with_dates(self) -> Dict[str, str]:
        """Get DEAD stores with their first dead dates"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            cur.execute('''
                SELECT url, first_dead_date
                FROM stores
                WHERE status = 'DEAD' AND first_dead_date IS NOT NULL
                ORDER BY first_dead_date DESC
            ''')

            dead_stores = {}
            for url, first_dead_date in cur.fetchall():
                # Ensure date is timezone-aware before converting to isoformat
                if first_dead_date and first_dead_date.tzinfo is None:
                    # If timezone is missing, assume it's UTC and convert to Pacific
                    utc_now = first_dead_date.replace(tzinfo=pytz.UTC)
                    pacific_tz = self.get_timezone()
                    first_dead_date = utc_now.astimezone(pacific_tz)

                dead_stores[url] = first_dead_date.date().isoformat()

            return dead_stores
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_store_details(self, url: str) -> Optional[Dict[str, Any]]:
        """Get detailed information for a specific store"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            cur.execute('''
                SELECT url, status, first_check, last_check, first_dead_date, check_count, timezone_checked
                FROM stores
                WHERE url = %s
            ''', (url,))

            result = cur.fetchone()
            if result:
                url, status, first_check, last_check, first_dead_date, check_count, timezone_checked = result
                return {
                    'url': url,
                    'status': status,
                    'first_check': first_check.isoformat() if first_check else None,
                    'last_check': last_check.isoformat() if last_check else None,
                    'first_dead_date': first_dead_date.isoformat() if first_dead_date else None,
                    'check_count': check_count,
                    'timezone_checked': timezone_checked
                }
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_check_history(self, url: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get check history for a specific store"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            cur.execute('''
                SELECT ch.status, ch.checked_at, ch.response_time, ch.status_code
                FROM check_history ch
                JOIN stores s ON ch.store_id = s.id
                WHERE s.url = %s
                ORDER BY ch.checked_at DESC
                LIMIT %s
            ''', (url, limit))

            history = []
            for status, checked_at, response_time, status_code in cur.fetchall():
                history.append({
                    'status': status,
                    'timestamp': checked_at.isoformat(),
                    'response_time': response_time,
                    'status_code': status_code
                })

            return history
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def clear_all_data(self) -> None:
        """Clear all data"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute('DELETE FROM check_history')
            cur.execute('DELETE FROM stores')
            conn.commit()
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def remove_store(self, url: str) -> bool:
        """Remove a specific store from database"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute('DELETE FROM stores WHERE url = %s', (url,))
            deleted = cur.rowcount > 0
            conn.commit()
            return deleted
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def bulk_delete_by_status(self, statuses: List[str]) -> int:
        """Bulk delete stores by status (much faster than individual deletes)"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute('DELETE FROM stores WHERE status = ANY(%s)', (statuses,))
            deleted_count = cur.rowcount
            conn.commit()
            return deleted_count
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_status_changes(self, days: int = 7) -> List[Dict[str, Any]]:
        """Get stores that changed status in the last N days"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            # Compute LAG over full history, then filter for changes within the time window
            # Ensure dates are handled with the correct timezone
            cur.execute('''
                WITH all_history AS (
                    SELECT
                        s.url,
                        ch.status,
                        ch.checked_at,
                        LAG(ch.status) OVER (PARTITION BY s.id ORDER BY ch.checked_at) as prev_status
                    FROM stores s
                    JOIN check_history ch ON s.id = ch.store_id
                ),
                changes_in_window AS (
                    SELECT url, prev_status, status, checked_at
                    FROM all_history
                    WHERE prev_status IS NOT NULL
                      AND prev_status != status
                      AND checked_at >= (CURRENT_TIMESTAMP AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles') - INTERVAL '%s days'
                )
                SELECT url, prev_status, status, checked_at
                FROM changes_in_window
                ORDER BY checked_at DESC
            ''', (days,))

            changes = []
            for url, prev_status, new_status, checked_at in cur.fetchall():
                changes.append({
                    'url': url,
                    'from_status': prev_status,
                    'to_status': new_status,
                    'changed_at': checked_at.isoformat()
                })

            return changes
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_latest_changes(self, minutes: int = 60) -> List[Dict[str, Any]]:
        """Get status changes from the last N minutes (for real-time notifications)"""
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()

            # Ensure dates are handled with the correct timezone
            cur.execute('''
                WITH all_history AS (
                    SELECT
                        s.url,
                        ch.status,
                        ch.checked_at,
                        LAG(ch.status) OVER (PARTITION BY s.id ORDER BY ch.checked_at) as prev_status
                    FROM stores s
                    JOIN check_history ch ON s.id = ch.store_id
                ),
                recent_changes AS (
                    SELECT url, prev_status, status, checked_at
                    FROM all_history
                    WHERE prev_status IS NOT NULL
                      AND prev_status != status
                      AND checked_at >= (CURRENT_TIMESTAMP AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles') - INTERVAL '%s minutes'
                )
                SELECT url, prev_status, status, checked_at
                FROM recent_changes
                ORDER BY checked_at DESC
            ''', (minutes,))

            changes = []
            for url, prev_status, new_status, checked_at in cur.fetchall():
                changes.append({
                    'url': url,
                    'from_status': prev_status,
                    'to_status': new_status,
                    'changed_at': checked_at.isoformat()
                })

            return changes
        finally:
            if cur:
                cur.close()
            if conn:
                self.return_connection(conn)

    def get_newly_dead_stores(self, minutes: int = 60) -> List[str]:
        """Get stores that became DEAD in the last N minutes"""
        changes = self.get_latest_changes(minutes)
        return [c['url'] for c in changes if c['to_status'] == 'DEAD']
