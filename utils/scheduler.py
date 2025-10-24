
import threading
import time
from datetime import datetime, timedelta
from typing import Callable, Optional
import os

class CheckScheduler:
    """Handle scheduled automatic checks of stores"""
    
    def __init__(self):
        self.running = False
        self.thread: Optional[threading.Thread] = None
        self.check_interval_minutes = int(os.getenv('CHECK_INTERVAL_MINUTES', '60'))
        self.last_check_time: Optional[datetime] = None
        self.check_callback: Optional[Callable] = None
    
    def set_check_callback(self, callback: Callable):
        """Set the callback function to run on each check"""
        self.check_callback = callback
    
    def start(self):
        """Start the scheduler"""
        if self.running:
            print("Scheduler already running")
            return False
        
        if not self.check_callback:
            print("No check callback set")
            return False
        
        self.running = True
        self.thread = threading.Thread(target=self._run_scheduler, daemon=True)
        self.thread.start()
        print(f"✅ Scheduler started - will check every {self.check_interval_minutes} minutes")
        return True
    
    def stop(self):
        """Stop the scheduler"""
        if not self.running:
            return False
        
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)
        print("⏸️ Scheduler stopped")
        return True
    
    def _run_scheduler(self):
        """Main scheduler loop"""
        while self.running:
            try:
                # Wait for the interval
                time.sleep(self.check_interval_minutes * 60)
                
                if not self.running:
                    break
                
                # Run the check
                print(f"🔄 Scheduled check started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                self.last_check_time = datetime.now()
                
                if self.check_callback:
                    self.check_callback()
                
                print(f"✅ Scheduled check completed")
                
            except Exception as e:
                print(f"Error in scheduler: {e}")
                time.sleep(60)  # Wait a minute before retrying
    
    def get_status(self) -> dict:
        """Get scheduler status"""
        return {
            'running': self.running,
            'interval_minutes': self.check_interval_minutes,
            'last_check': self.last_check_time.isoformat() if self.last_check_time else None,
            'next_check': (self.last_check_time + timedelta(minutes=self.check_interval_minutes)).isoformat() 
                         if self.last_check_time else None
        }
    
    def set_interval(self, minutes: int):
        """Change check interval"""
        if minutes < 1:
            return False
        
        self.check_interval_minutes = minutes
        print(f"Check interval updated to {minutes} minutes")
        return True
