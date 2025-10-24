
import os
import requests
from typing import List, Dict, Any
from datetime import datetime

class TelegramNotifier:
    """Handle Telegram notifications for store status changes"""
    
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.enabled = bool(self.bot_token and self.chat_id)
        
        if not self.enabled:
            print("⚠️ Telegram notifications disabled: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set")
    
    def send_message(self, message: str) -> bool:
        """Send a message to Telegram"""
        if not self.enabled:
            return False
        
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(url, json=payload, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f"Error sending Telegram message: {e}")
            return False
    
    def notify_dead_stores(self, dead_stores: List[str]) -> bool:
        """Notify about newly dead stores"""
        if not dead_stores:
            return True
        
        message = f"🔴 <b>New DEAD Stores Detected</b>\n\n"
        message += f"Found {len(dead_stores)} newly dead store(s):\n\n"
        
        for i, url in enumerate(dead_stores[:10], 1):  # Limit to 10 to avoid message too long
            message += f"{i}. {url}\n"
        
        if len(dead_stores) > 10:
            message += f"\n... and {len(dead_stores) - 10} more"
        
        message += f"\n\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        return self.send_message(message)
    
    def notify_status_changes(self, changes: List[Dict[str, Any]]) -> bool:
        """Notify about status changes"""
        if not changes:
            return True
        
        message = f"🔄 <b>Store Status Changes</b>\n\n"
        
        # Group by change type
        to_dead = [c for c in changes if c['to_status'] == 'DEAD']
        to_live = [c for c in changes if c['to_status'] == 'LIVE' and c['from_status'] == 'DEAD']
        to_unpaid = [c for c in changes if c['to_status'] == 'UNPAID']
        
        if to_dead:
            message += f"🔴 Newly DEAD ({len(to_dead)}):\n"
            for change in to_dead[:5]:
                message += f"• {change['url']}\n"
            if len(to_dead) > 5:
                message += f"... and {len(to_dead) - 5} more\n"
            message += "\n"
        
        if to_live:
            message += f"🟢 Recovered to LIVE ({len(to_live)}):\n"
            for change in to_live[:5]:
                message += f"• {change['url']}\n"
            if len(to_live) > 5:
                message += f"... and {len(to_live) - 5} more\n"
            message += "\n"
        
        if to_unpaid:
            message += f"🟡 Now UNPAID ({len(to_unpaid)}):\n"
            for change in to_unpaid[:5]:
                message += f"• {change['url']}\n"
            if len(to_unpaid) > 5:
                message += f"... and {len(to_unpaid) - 5} more\n"
        
        message += f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        return self.send_message(message)
    
    def test_connection(self) -> bool:
        """Test Telegram connection"""
        if not self.enabled:
            return False
        
        message = "✅ Telegram notification is working!\n\nShopify Store Monitor is connected."
        return self.send_message(message)
