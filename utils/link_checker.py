import requests
import time
import random
import os
from typing import Dict, Any, List, Optional
from urllib.parse import urlparse
from datetime import datetime
import pytz

class ShopifyChecker:
    """Handle Shopify store status checking with proxy support (HTTP/HTTPS/SOCKS5) and enhanced reliability"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.timeout = 10
        self.retry_delay = 2
        
        # Proxy configuration
        self.proxies_list = self._load_proxies()
        self.current_proxy_index = 0
        self.use_proxy = len(self.proxies_list) > 0
        
        # Manual proxy override (for UI picker)
        self.manual_proxy = None
        
        # Random delay configuration (in seconds)
        self.min_delay = float(os.getenv('CHECK_MIN_DELAY', '0.5'))
        self.max_delay = float(os.getenv('CHECK_MAX_DELAY', '2.0'))
        
        # Smart US timezone-aware delay
        self.use_smart_delay = os.getenv('USE_SMART_DELAY', 'true').lower() == 'true'
        self.us_timezones = [
            'America/Los_Angeles',  # PST/PDT (West Coast)
            'America/Denver',       # MST/MDT (Mountain)
            'America/Chicago',      # CST/CDT (Central)
            'America/New_York'      # EST/EDT (East Coast)
        ]
    
    def _parse_proxy_url(self, proxy_url: str) -> Dict[str, str]:
        """
        Parse proxy URL and return dict compatible with requests library
        Supports: http://, https://, socks5://, socks5h://
        
        Examples:
        - http://user:pass@host:port
        - https://user:pass@host:port
        - socks5://127.0.0.1:60000
        - socks5://user:pass@host:port
        """
        proxy_url = proxy_url.strip()
        parsed = urlparse(proxy_url)
        
        # Handle SOCKS5
        if parsed.scheme in ['socks5', 'socks5h']:
            # requests library supports socks5:// directly with PySocks
            return {
                'http': proxy_url,
                'https': proxy_url
            }
        
        # Handle HTTP/HTTPS
        elif parsed.scheme in ['http', 'https']:
            return {
                'http': proxy_url,
                'https': proxy_url
            }
        
        # If no scheme, assume HTTP
        elif not parsed.scheme:
            default_url = f'http://{proxy_url}'
            return {
                'http': default_url,
                'https': default_url
            }
        
        else:
            # Unknown scheme, try as-is
            return {
                'http': proxy_url,
                'https': proxy_url
            }
    
    def _load_proxies(self) -> List[Dict[str, str]]:
        """Load proxy configuration from environment variables"""
        proxies = []
        
        # Support for single proxy
        proxy_url = os.getenv('PROXY_URL')
        if proxy_url:
            proxies.append(self._parse_proxy_url(proxy_url))
        
        # Support for multiple proxies (comma-separated)
        proxy_list = os.getenv('PROXY_LIST')
        if proxy_list:
            proxy_urls = [p.strip() for p in proxy_list.split(',') if p.strip()]
            for proxy_url in proxy_urls:
                proxies.append(self._parse_proxy_url(proxy_url))
        
        return proxies
    
    def set_manual_proxy(self, proxy_url: Optional[str]):
        """
        Set manual proxy override (for UI picker)
        Set to None to disable manual proxy
        """
        if proxy_url and proxy_url.strip():
            self.manual_proxy = self._parse_proxy_url(proxy_url)
        else:
            self.manual_proxy = None
    
    def get_manual_proxy(self) -> Optional[str]:
        """Get current manual proxy URL"""
        if self.manual_proxy:
            # Return one of the values (they should be the same)
            return self.manual_proxy.get('http') or self.manual_proxy.get('https')
        return None
    
    def _get_next_proxy(self) -> Optional[Dict[str, str]]:
        """Get next proxy using round-robin rotation or manual proxy"""
        # Manual proxy takes precedence
        if self.manual_proxy:
            return self.manual_proxy
        
        # Otherwise use auto-rotation
        if not self.use_proxy or not self.proxies_list:
            return None
        
        proxy = self.proxies_list[self.current_proxy_index]
        self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxies_list)
        return proxy
    
    def get_proxy_info(self) -> Dict[str, Any]:
        """Get current proxy configuration info"""
        return {
            'enabled': self.use_proxy or (self.manual_proxy is not None),
            'total_proxies': len(self.proxies_list),
            'current_index': self.current_proxy_index,
            'min_delay': self.min_delay,
            'max_delay': self.max_delay,
            'manual_proxy': self.get_manual_proxy(),
            'has_manual_proxy': self.manual_proxy is not None
        }
    
    def get_us_timezone_status(self) -> Dict[str, Any]:
        """Get current time and business hours status across US timezones"""
        status = {}
        
        for tz_name in self.us_timezones:
            tz = pytz.timezone(tz_name)
            from datetime import datetime as dt
            utc_now = dt.utcnow().replace(tzinfo=pytz.UTC)
            local_time = utc_now.astimezone(tz)
            hour = local_time.hour
            
            # Determine if it's business hours
            is_business_hours = 9 <= hour <= 17
            is_peak_hours = 9 <= hour <= 17
            is_off_hours = hour < 8 or hour > 22
            
            status[tz_name.split('/')[-1]] = {
                'current_time': local_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
                'hour': hour,
                'is_business_hours': is_business_hours,
                'is_peak_hours': is_peak_hours,
                'is_off_hours': is_off_hours
            }
        
        return {
            'timezones': status,
            'smart_delay_enabled': self.use_smart_delay,
            'current_multiplier': self._get_random_us_timezone_factor()
        }
    
    def _get_random_us_timezone_factor(self) -> float:
        """
        Calculate delay multiplier based on a RANDOM US timezone.
        This simulates natural user behavior from different US regions.
        """
        if not self.use_smart_delay:
            return 1.0
        
        # Randomly pick one US timezone to simulate user from that region
        random_tz_name = random.choice(self.us_timezones)
        tz = pytz.timezone(random_tz_name)
        from datetime import datetime as dt
        utc_now = dt.utcnow().replace(tzinfo=pytz.UTC)
        local_time = utc_now.astimezone(tz)
        hour = local_time.hour
        
        # Determine delay based on this random timezone's local time
        if 9 <= hour <= 17:
            # Peak business hours in this timezone
            return random.uniform(2.0, 2.5)
        elif hour < 8 or hour > 22:
            # Off-peak hours (night/early morning)
            return 1.0
        else:
            # Normal hours
            return random.uniform(1.3, 1.7)
    
    def _random_delay(self):
        """
        Add smart random delay between requests to avoid detection.
        Randomly picks a US timezone and adjusts delay accordingly.
        This simulates natural traffic from different US regions.
        """
        # Get base delay
        base_delay = random.uniform(self.min_delay, self.max_delay)
        
        # Apply smart multiplier based on RANDOM US timezone
        multiplier = self._get_random_us_timezone_factor()
        
        # Add random jitter to make pattern unpredictable
        jitter = random.uniform(0.8, 1.2)
        
        final_delay = base_delay * multiplier * jitter
        
        # Cap maximum delay at 10 seconds to avoid too long waits
        final_delay = min(final_delay, 10.0)
        
        time.sleep(final_delay)

    def check_store_status(self, url: str) -> str:
        """
        Check the status of a Shopify store with proxy support (HTTP/HTTPS/SOCKS5)
        Returns: LIVE, DEAD, UNPAID, or UNKNOWN
        """
        try:
            # Ensure URL has proper format
            if not url.startswith('http'):
                url = f'https://{url}'
            
            # Get proxy for this request
            proxy = self._get_next_proxy()
            
            # Make request with timeout and optional proxy
            response = self.session.get(
                url, 
                timeout=self.timeout,
                proxies=proxy,
                allow_redirects=True
            )
            html_content = response.text.lower()
            status_code = response.status_code
            
            # Check response status and content
            if status_code == 200:
                # Check for specific Shopify messages
                unpaid_indicators = [
                    "sorry, this store is currently unavailable",
                    "this store is unavailable", 
                    "store is temporarily unavailable",
                    "this shop is currently unavailable"
                ]
                
                if any(indicator in html_content for indicator in unpaid_indicators):
                    return "UNPAID"
                
                # Check if it's a valid Shopify store page
                shopify_indicators = [
                    "shopify",
                    "powered by shopify",
                    "cdn.shopify.com",
                    "shop.js"
                ]
                
                if any(indicator in html_content for indicator in shopify_indicators):
                    return "LIVE"
                else:
                    # Might be a redirect or different content
                    return "LIVE"
            
            elif status_code == 404:
                return "DEAD"
            elif status_code == 403:
                return "UNPAID"
            elif status_code >= 500:
                # Server error - might be temporary
                return "UNKNOWN"
            else:
                return f"UNKNOWN ({status_code})"
                
        except requests.exceptions.ProxyError as e:
            # Proxy failed, try without proxy if available
            print(f"Proxy error: {e}")
            if self.use_proxy or self.manual_proxy:
                try:
                    response = self.session.get(url, timeout=self.timeout)
                    # Retry without proxy
                    return self._analyze_response(response)
                except:
                    return "DEAD"
            return "DEAD"
        except requests.exceptions.Timeout:
            return "DEAD"
        except requests.exceptions.ConnectionError:
            return "DEAD" 
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return "DEAD"
        except Exception as e:
            print(f"Unknown error: {e}")
            return "UNKNOWN"
    
    def _analyze_response(self, response) -> str:
        """Analyze response to determine store status"""
        html_content = response.text.lower()
        status_code = response.status_code
        
        if status_code == 200:
            unpaid_indicators = [
                "sorry, this store is currently unavailable",
                "this store is unavailable", 
                "store is temporarily unavailable",
                "this shop is currently unavailable"
            ]
            
            if any(indicator in html_content for indicator in unpaid_indicators):
                return "UNPAID"
            
            shopify_indicators = [
                "shopify",
                "powered by shopify",
                "cdn.shopify.com",
                "shop.js"
            ]
            
            if any(indicator in html_content for indicator in shopify_indicators):
                return "LIVE"
            else:
                return "LIVE"
        elif status_code == 404:
            return "DEAD"
        elif status_code == 403:
            return "UNPAID"
        elif status_code >= 500:
            return "UNKNOWN"
        else:
            return f"UNKNOWN ({status_code})"

    def batch_check_stores(self, urls: list, progress_callback=None) -> Dict[str, str]:
        """
        Check multiple stores with progress tracking and random delays
        """
        results = {}
        total = len(urls)
        
        for i, url in enumerate(urls):
            if progress_callback:
                progress_callback(i + 1, total, url)
            
            results[url] = self.check_store_status(url)
            
            # Random delay between requests to avoid detection
            if i < total - 1:  # Don't delay after last item
                self._random_delay()
        
        return results

    def verify_dead_store(self, url: str) -> str:
        """
        Perform a more thorough check for suspected dead stores
        """
        # First check
        first_result = self.check_store_status(url)
        
        if first_result != "DEAD":
            return first_result
        
        # Wait and check again with different proxy
        time.sleep(self.retry_delay)
        second_result = self.check_store_status(url)
        
        # If still dead after second check, it's confirmed dead
        return second_result
