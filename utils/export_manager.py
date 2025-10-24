import os
from datetime import datetime
from typing import Dict, List, Any

class ExportManager:
    """Handle data export functionality"""
    
    def __init__(self):
        self.export_dir = "exports"
        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)

    def export_data(self, data_manager, export_type: str) -> str:
        """
        Export data based on type
        Returns filename of exported file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if export_type == "All Data":
            return self._export_all_data(data_manager, timestamp)
        elif export_type == "LIVE Only":
            return self._export_by_status(data_manager, "LIVE", timestamp)
        elif export_type == "DEAD Only":
            return self._export_dead_stores(data_manager, timestamp)
        elif export_type == "UNPAID Only":
            return self._export_by_status(data_manager, "UNPAID", timestamp)
        
        return None

    def _export_all_data(self, data_manager, timestamp: str) -> str:
        """Export all data with full details"""
        filename = os.path.join(self.export_dir, f"all_stores_{timestamp}.txt")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("SHOPIFY STORE MONITORING REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Summary statistics
            status_counts = data_manager.get_status_counts()
            total = data_manager.get_total_count()
            
            f.write("SUMMARY:\n")
            f.write(f"Total Stores: {total}\n")
            for status, count in status_counts.items():
                percentage = (count / total * 100) if total > 0 else 0
                f.write(f"{status}: {count} ({percentage:.1f}%)\n")
            f.write("\n")
            
            # Detailed listing
            data = data_manager.get_data()
            for status in ["LIVE", "DEAD", "UNPAID", "UNCHECKED"]:
                stores = [url for url, store_data in data.items() if store_data.get('status') == status]
                if stores:
                    f.write(f"\n{status} STORES ({len(stores)}):\n")
                    f.write("-" * 30 + "\n")
                    for url in sorted(stores):
                        store_data = data[url]
                        f.write(f"{url}")
                        if store_data.get('last_check'):
                            f.write(f" (Last check: {store_data['last_check'][:19]})")
                        if status == "DEAD" and store_data.get('first_dead_date'):
                            f.write(f" (Dead since: {store_data['first_dead_date'][:10]})")
                        f.write("\n")
        
        return filename

    def _export_by_status(self, data_manager, status: str, timestamp: str) -> str:
        """Export stores by specific status"""
        filename = os.path.join(self.export_dir, f"{status.lower()}_stores_{timestamp}.txt")
        
        stores = data_manager.get_stores_by_status(status)
        data = data_manager.get_data()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"{status} SHOPIFY STORES\n")
            f.write("=" * 30 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total {status} stores: {len(stores)}\n\n")
            
            for url in sorted(stores):
                store_data = data[url]
                f.write(f"{url}")
                if store_data.get('last_check'):
                    f.write(f" (Checked: {store_data['last_check'][:19]})")
                f.write("\n")
        
        return filename

    def _export_dead_stores(self, data_manager, timestamp: str) -> str:
        """Export DEAD stores with death dates"""
        filename = os.path.join(self.export_dir, f"dead_stores_{timestamp}.txt")
        
        dead_stores = data_manager.get_dead_stores_with_dates()
        data = data_manager.get_data()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("DEAD SHOPIFY STORES\n")
            f.write("=" * 30 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total DEAD stores: {len(dead_stores)}\n\n")
            
            # Group by death date
            by_date = {}
            for url, death_date in dead_stores.items():
                if death_date not in by_date:
                    by_date[death_date] = []
                by_date[death_date].append(url)
            
            for death_date in sorted(by_date.keys(), reverse=True):
                f.write(f"\nDied on {death_date} ({len(by_date[death_date])} stores):\n")
                f.write("-" * 40 + "\n")
                for url in sorted(by_date[death_date]):
                    store_data = data[url]
                    f.write(f"{url}")
                    if store_data.get('check_count', 0) > 1:
                        f.write(f" (Checked {store_data['check_count']} times)")
                    f.write("\n")
            
            # Also list URLs only for easy copying
            f.write(f"\n\nURLs ONLY (for easy copying):\n")
            f.write("-" * 30 + "\n")
            for url in sorted(dead_stores.keys()):
                f.write(f"{url}\n")
        
        return filename

    def export_simple_list(self, urls: List[str], filename_prefix: str) -> str:
        """Export simple list of URLs"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.export_dir, f"{filename_prefix}_{timestamp}.txt")
        
        with open(filename, 'w', encoding='utf-8') as f:
            for url in urls:
                f.write(f"{url}\n")
        
        return filename
