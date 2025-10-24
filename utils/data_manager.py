import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

class DataManager:
    """Handle data persistence and management for store checking"""
    
    def __init__(self, data_file: str = "shopify_data.json"):
        self.data_file = data_file
        self.data: Dict[str, Dict[str, Any]] = {}
        self.load_from_file()

    def load_urls(self, urls: List[str]) -> None:
        """Load new URLs into the system"""
        for url in urls:
            url = url.strip()
            if url and url not in self.data:
                self.data[url] = {
                    'status': 'UNCHECKED',
                    'first_check': None,
                    'last_check': None,
                    'first_dead_date': None,
                    'check_count': 0,
                    'check_history': []
                }
        self.save_to_file()

    def update_store_status(self, url: str, status: str) -> None:
        """Update store status with timestamp and history tracking"""
        current_time = datetime.now().isoformat()
        
        if url not in self.data:
            self.data[url] = {
                'status': status,
                'first_check': current_time,
                'last_check': current_time,
                'first_dead_date': None,
                'check_count': 1,
                'check_history': []
            }
        else:
            old_status = self.data[url].get('status', 'UNCHECKED')
            self.data[url]['status'] = status
            self.data[url]['last_check'] = current_time
            self.data[url]['check_count'] += 1
            
            # Set first check time if not set
            if not self.data[url].get('first_check'):
                self.data[url]['first_check'] = current_time
            
            # Track first dead date
            if status == 'DEAD' and old_status != 'DEAD':
                self.data[url]['first_dead_date'] = current_time
            elif status != 'DEAD' and old_status == 'DEAD':
                # Store came back to life, clear dead date
                self.data[url]['first_dead_date'] = None
        
        # Add to history
        self.data[url]['check_history'].append({
            'timestamp': current_time,
            'status': status
        })
        
        # Keep only last 50 history entries to prevent file bloat
        if len(self.data[url]['check_history']) > 50:
            self.data[url]['check_history'] = self.data[url]['check_history'][-50:]
        
        self.save_to_file()

    def get_data(self) -> Dict[str, Dict[str, Any]]:
        """Get all data"""
        return self.data

    def get_stores_by_status(self, status: str) -> List[str]:
        """Get list of URLs with specific status"""
        return [url for url, data in self.data.items() if data.get('status') == status]

    def get_status_counts(self) -> Dict[str, int]:
        """Get count of stores by status"""
        counts = {}
        for url, data in self.data.items():
            status = data.get('status', 'UNCHECKED')
            counts[status] = counts.get(status, 0) + 1
        return counts

    def get_total_count(self) -> int:
        """Get total number of stores"""
        return len(self.data)

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
        filtered = {}
        
        for url, data in self.data.items():
            # Status filter
            if data.get('status', 'UNCHECKED') not in status_filters:
                continue
            
            # Search filter
            if search_term and search_term.lower() not in url.lower():
                continue
            
            filtered[url] = data
        
        return filtered

    def get_timeline_data(self) -> List[Dict[str, Any]]:
        """Get timeline data for charts"""
        timeline = {}
        
        for url, data in self.data.items():
            for history_entry in data.get('check_history', []):
                date = history_entry['timestamp'][:10]  # Extract date part
                status = history_entry['status']
                
                if date not in timeline:
                    timeline[date] = {}
                
                timeline[date][status] = timeline[date].get(status, 0) + 1
        
        # Convert to list format for charts
        timeline_list = []
        for date, status_counts in sorted(timeline.items()):
            for status, count in status_counts.items():
                timeline_list.append({
                    'date': date,
                    'status': status,
                    'count': count
                })
        
        return timeline_list

    def get_dead_stores_with_dates(self) -> Dict[str, str]:
        """Get DEAD stores with their first dead dates"""
        dead_stores = {}
        for url, data in self.data.items():
            if data.get('status') == 'DEAD' and data.get('first_dead_date'):
                dead_date = data['first_dead_date'][:10]  # Extract date part
                dead_stores[url] = dead_date
        return dead_stores

    def save_to_file(self) -> bool:
        """Save data to JSON file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def load_from_file(self) -> bool:
        """Load data from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
                return True
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            self.data = {}
            return False

    def clear_all_data(self) -> None:
        """Clear all data"""
        self.data = {}
        self.save_to_file()

    def remove_store(self, url: str) -> bool:
        """Remove a specific store from data"""
        if url in self.data:
            del self.data[url]
            self.save_to_file()
            return True
        return False

    def get_store_details(self, url: str) -> Optional[Dict[str, Any]]:
        """Get detailed information for a specific store"""
        return self.data.get(url)
