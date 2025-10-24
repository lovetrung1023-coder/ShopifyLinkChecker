"""
Migration script to move data from JSON to PostgreSQL
"""
import json
import os
from utils.db_manager import DatabaseManager
from datetime import datetime

def migrate_json_to_db():
    """Migrate data from shopify_data.json to PostgreSQL"""
    
    json_file = "shopify_data.json"
    
    if not os.path.exists(json_file):
        print("No JSON file found. Starting with fresh database.")
        return
    
    print(f"Loading data from {json_file}...")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    print(f"Found {len(json_data)} stores in JSON file")
    
    # Initialize database manager
    db = DatabaseManager()
    
    print("Migrating data to PostgreSQL...")
    
    migrated = 0
    for url, data in json_data.items():
        try:
            # Load URL first
            db.load_urls([url])
            
            # Update with full data
            status = data.get('status', 'UNCHECKED')
            
            # We'll use update_store_status which handles everything
            # But we need to preserve the original timestamps
            # For this migration, we'll need direct SQL
            
            import psycopg2
            conn = db.get_connection()
            cur = conn.cursor()
            
            try:
                # Get store ID
                cur.execute('SELECT id FROM stores WHERE url = %s', (url,))
                result = cur.fetchone()
                
                if result:
                    store_id = result[0]
                    
                    # Update with preserved timestamps
                    first_check = data.get('first_check')
                    last_check = data.get('last_check')
                    first_dead_date = data.get('first_dead_date')
                    check_count = data.get('check_count', 0)
                    
                    # Use first_check as created_at and last_check as updated_at for historical accuracy
                    created_at = first_check if first_check else datetime.now().isoformat()
                    updated_at = last_check if last_check else datetime.now().isoformat()
                    
                    cur.execute('''
                        UPDATE stores
                        SET status = %s,
                            first_check = %s,
                            last_check = %s,
                            first_dead_date = %s,
                            check_count = %s,
                            created_at = %s,
                            updated_at = %s
                        WHERE id = %s
                    ''', (status, first_check, last_check, first_dead_date, check_count, 
                          created_at, updated_at, store_id))
                    
                    # Migrate check history
                    check_history = data.get('check_history', [])
                    for history_entry in check_history:
                        timestamp = history_entry.get('timestamp')
                        hist_status = history_entry.get('status')
                        
                        cur.execute('''
                            INSERT INTO check_history (store_id, status, checked_at)
                            VALUES (%s, %s, %s)
                        ''', (store_id, hist_status, timestamp))
                    
                    conn.commit()
                    migrated += 1
                    
                    if migrated % 50 == 0:
                        print(f"Migrated {migrated} stores...")
            
            finally:
                cur.close()
                conn.close()
        
        except Exception as e:
            print(f"Error migrating {url}: {e}")
            continue
    
    print(f"\n✅ Migration completed!")
    print(f"Successfully migrated {migrated} stores to PostgreSQL")
    
    # Backup JSON file
    backup_file = f"{json_file}.backup"
    if os.path.exists(json_file):
        os.rename(json_file, backup_file)
        print(f"Original JSON file backed up to {backup_file}")

if __name__ == "__main__":
    migrate_json_to_db()
