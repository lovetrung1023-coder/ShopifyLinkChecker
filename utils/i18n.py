"""Internationalization support for the application"""

TRANSLATIONS = {
    'vi': {
        # Header
        'title': '🛍️ Shopify Store Monitor',
        'control_panel': '🔧 Bảng Điều Khiển',

        # Input Methods
        'input_methods': '📥 Phương Thức Nhập',
        'choose_input': 'Chọn phương thức nhập:',
        'upload_file': 'Tải File Lên',
        'manual_input': 'Nhập Thủ Công',
        'choose_file': 'Chọn file .txt',
        'file_help': 'Tải lên file text với mỗi URL trên một dòng',
        'file_contains': 'File chứa {count} URLs',
        'load_urls_file': 'Load URLs từ File',
        'loading_urls': '⏳ Đang load {count} URLs vào database...',
        'loaded_success': '✅ Đã load {count} URLs!',
        'enter_urls': 'Nhập URLs (mỗi dòng một URL):',
        'enter_urls_help': 'Nhập URL Shopify, mỗi dòng một URL',
        'load_manual': 'Load URLs Thủ Công',

        # Check Controls
        'check_controls': '🔍 Điều Khiển Kiểm Tra',
        'start_checking': '🚀 Bắt Đầu Kiểm Tra Tất Cả',
        'recheck_dead': '🔄 Kiểm Tra Lại DEAD Stores',
        'no_urls': 'Không có URL để kiểm tra!',
        'no_dead': 'Không có DEAD stores để kiểm tra lại',

        # Scheduler
        'scheduler': '⏰ Lịch Kiểm Tra Tự Động',
        'stop_scheduler': '⏸️ Dừng Lịch',
        'start_scheduler': '▶️ Khởi Động Lịch',
        'interval': 'Khoảng thời gian (phút):',
        'scheduler_running': '✅ Đang chạy - Kiểm tra tiếp theo lúc {time}',
        'scheduler_stopped': '⏸️ Lịch đã dừng',

        # Telegram
        'telegram': '📱 Thông Báo Telegram',
        'telegram_connected': '✅ Telegram đã kết nối',
        'test_telegram': '🧪 Kiểm Tra Telegram',
        'test_sent': 'Tin nhắn kiểm tra đã gửi!',
        'test_failed': 'Không thể gửi tin nhắn kiểm tra',
        'telegram_not_configured': '⚠️ Telegram chưa được cấu hình',
        'setup_instructions': 'Hướng Dẫn Cài Đặt',

        # Export
        'export_data': '📤 Xuất Dữ Liệu',
        'export_type': 'Loại xuất:',
        'all_data': 'Tất Cả Dữ Liệu',
        'live_only': 'Chỉ LIVE',
        'dead_only': 'Chỉ DEAD',
        'unpaid_only': 'Chỉ UNPAID',
        'download_export': 'Tải Xuất Dữ Liệu',
        'exporting': '📤 Đang xuất dữ liệu...',
        'export_success': '✅ Xuất dữ liệu thành công: {type}',

        # Delete
        'delete_links': '🗑️ Xóa Links',
        'delete_warning': '⚠️ Hành động này không thể hoàn tác!',
        'choose_delete': 'Chọn mục cần xóa:',
        'select_option': 'Chọn tùy chọn...',
        'all_checked': 'Tất Cả Links Đã Kiểm Tra',
        'dead_links': 'Chỉ DEAD Links',
        'live_links': 'Chỉ LIVE Links',
        'unpaid_links': 'Chỉ UNPAID Links',
        'unchecked_links': 'Chỉ UNCHECKED Links',
        'will_delete': 'Sẽ xóa {count} links',
        'confirm_delete': 'Tôi xác nhận xóa {count} links',
        'delete_now': '🗑️ Xóa Ngay',
        'deleting': '🗑️ Đang xóa...',
        'deleted_success': '✅ Đã xóa {count} links!',
        'no_links_delete': 'Không có link nào để xóa',

        # Settings
        'settings': '⚙️ Cài Đặt',
        'theme': 'Giao Diện',
        'language': 'Ngôn Ngữ',
        'dark_theme': '🌙 Tối',
        'light_theme': '☀️ Sáng',

        # Metrics
        'total_stores': 'Tổng Stores',
        'live_stores': 'LIVE Stores',
        'dead_stores': 'DEAD Stores',
        'unpaid_stores': 'UNPAID Stores',

        # Charts
        'overview': '📊 Tổng Quan',
        'trends': '📈 Xu Hướng',
        'changes': '🔄 Thay Đổi',
        'comparison': '🔍 So Sánh',
        'status_distribution': 'Phân Bố Trạng Thái',
        'status_composition':
        'Cấu Trúc Trạng Thái Theo Thời Gian (Trong {days} Ngày)',
        'status_trends': 'Xu Hướng Trạng Thái Riêng Lẻ (Trong {days} Ngày)',
        'recent_changes': 'Thay Đổi Trạng Thái Gần Đây',
        'time_range': 'Khoảng Thời Gian:',
        'last_n_days': '{days} ngày qua',
        'no_timeline_data': 'Không có dữ liệu cho {days} ngày qua',
        'show_changes': 'Hiển thị thay đổi từ N ngày trước:',
        'no_changes': 'Không phát hiện thay đổi trong {days} ngày qua',

        # Comparison
        'check_comparison': 'So Sánh Kết Quả Kiểm Tra',
        'compare_over': 'So sánh thay đổi trong:',
        'last_hour': 'Giờ Qua',
        'last_6_hours': '6 Giờ Qua',
        'last_24_hours': '24 Giờ Qua',
        'last_7_days': '7 Ngày Qua',
        'changes_in': 'Thay Đổi Trong {period}',
        'newly_dead': 'Mới DEAD',
        'recovered': 'Đã Phục Hồi',
        'total_changes': 'Tổng Thay Đổi',
        'send_summary': '📱 Gửi Tóm Tắt Telegram',
        'summary_sent': 'Tóm tắt đã gửi đến Telegram!',
        'summary_failed': 'Không thể gửi tin nhắn Telegram',
        'no_changes_period': 'Không phát hiện thay đổi trong {period}',

        # Filters
        'filter_status': 'Lọc theo Trạng Thái:',
        'search_urls': '🔍 Tìm URLs:',
        'search_placeholder': 'Nhập từ khóa tìm kiếm...',
        'clear_filters': 'Xóa Bộ Lọc',
        'showing': 'Hiển thị {current} trong tổng số {total} stores',
        'no_data': 'Không có dữ liệu khớp với bộ lọc hiện tại',

        # Table Headers
        'url': 'URL',
        'status': 'Trạng Thái',
        'last_check': 'Kiểm Tra Cuối',
        'first_dead_date': 'Ngày DEAD',
        'check_count': 'Số Lần Kiểm Tra',
        'store_url': 'URL Store',
        'from': 'Từ',
        'to': 'Đến',
        'changed_at': 'Thay Đổi Lúc',
        'change': 'Thay Đổi',

        # Progress Messages
        'checking': '🔍 Đang kiểm tra {current}/{total}: {url}...',
        'rechecking_dead': '🔄 Kiểm tra lại DEAD store: {url}...',
        'completed_check': '✅ Hoàn thành kiểm tra {count} stores!',
        'rechecked_dead': '✅ Đã kiểm tra lại {count} DEAD stores!',
        'error_deleting': 'Lỗi khi xóa: {error}',
    },
    'en': {
        # Header
        'title': '🛍️ Shopify Store Monitor',
        'control_panel': '🔧 Control Panel',

        # Input Methods
        'input_methods': '📥 Input Methods',
        'choose_input': 'Choose input method:',
        'upload_file': 'Upload File',
        'manual_input': 'Manual Input',
        'choose_file': 'Choose a .txt file',
        'file_help': 'Upload a text file with one URL per line',
        'file_contains': 'File contains {count} URLs',
        'load_urls_file': 'Load URLs from File',
        'loading_urls': '⏳ Loading {count} URLs into database...',
        'loaded_success': '✅ Loaded {count} URLs!',
        'enter_urls': 'Enter URLs (one per line):',
        'enter_urls_help': 'Enter Shopify URLs, one per line',
        'load_manual': 'Load Manual URLs',

        # Check Controls
        'check_controls': '🔍 Check Controls',
        'start_checking': '🚀 Start Checking All',
        'recheck_dead': '🔄 Recheck DEAD Stores',
        'no_urls': 'No URLs loaded!',
        'no_dead': 'No DEAD stores to recheck',

        # Scheduler
        'scheduler': '⏰ Auto-Check Scheduler',
        'stop_scheduler': '⏸️ Stop Scheduler',
        'start_scheduler': '▶️ Start Scheduler',
        'interval': 'Interval (min):',
        'scheduler_running': '✅ Running - Next check at {time}',
        'scheduler_stopped': '⏸️ Scheduler stopped',

        # Telegram
        'telegram': '📱 Telegram Notifications',
        'telegram_connected': '✅ Telegram connected',
        'test_telegram': '🧪 Test Telegram',
        'test_sent': 'Test message sent!',
        'test_failed': 'Failed to send test message',
        'telegram_not_configured': '⚠️ Telegram not configured',
        'setup_instructions': 'Setup Instructions',

        # Export
        'export_data': '📤 Export Data',
        'export_type': 'Export Type:',
        'all_data': 'All Data',
        'live_only': 'LIVE Only',
        'dead_only': 'DEAD Only',
        'unpaid_only': 'UNPAID Only',
        'download_export': 'Download Export',
        'exporting': '📤 Exporting data...',
        'export_success': '✅ Export successful: {type}',

        # Delete
        'delete_links': '🗑️ Delete Links',
        'delete_warning': '⚠️ This action cannot be undone!',
        'choose_delete': 'Choose what to delete:',
        'select_option': 'Select option...',
        'all_checked': 'All Checked Links',
        'dead_links': 'DEAD Links Only',
        'live_links': 'LIVE Links Only',
        'unpaid_links': 'UNPAID Links Only',
        'unchecked_links': 'UNCHECKED Links Only',
        'will_delete': 'Will delete {count} links',
        'confirm_delete': 'I confirm delete {count} links',
        'delete_now': '🗑️ Delete Now',
        'deleting': '🗑️ Deleting...',
        'deleted_success': '✅ Deleted {count} links!',
        'no_links_delete': 'No links to delete',

        # Settings
        'settings': '⚙️ Settings',
        'theme': 'Theme',
        'language': 'Language',
        'dark_theme': '🌙 Dark',
        'light_theme': '☀️ Light',

        # Metrics
        'total_stores': 'Total Stores',
        'live_stores': 'LIVE Stores',
        'dead_stores': 'DEAD Stores',
        'unpaid_stores': 'UNPAID Stores',

        # Charts
        'overview': '📊 Overview',
        'trends': '📈 Trends',
        'changes': '🔄 Changes',
        'comparison': '🔍 Comparison',
        'status_distribution': 'Store Status Distribution',
        'status_composition':
        'Status Composition Over Time (Last {days} Days)',
        'status_trends': 'Individual Status Trends (Last {days} Days)',
        'recent_changes': 'Recent Status Changes',
        'time_range': 'Time Range:',
        'last_n_days': 'Last {days} days',
        'no_timeline_data':
        'No timeline data available for the last {days} days',
        'show_changes': 'Show changes from last N days:',
        'no_changes': 'No status changes detected in the last {days} days',

        # Comparison
        'check_comparison': 'Check Results Comparison',
        'compare_over': 'Compare changes over:',
        'last_hour': 'Last Hour',
        'last_6_hours': 'Last 6 Hours',
        'last_24_hours': 'Last 24 Hours',
        'last_7_days': 'Last 7 Days',
        'changes_in': 'Changes in {period}',
        'newly_dead': 'Newly DEAD',
        'recovered': 'Recovered',
        'total_changes': 'Total Changes',
        'send_summary': '📱 Send Telegram Summary',
        'summary_sent': 'Summary sent to Telegram!',
        'summary_failed': 'Failed to send Telegram message',
        'no_changes_period': 'No changes detected in {period}',

        # Filters
        'filter_status': 'Filter by Status:',
        'search_urls': '🔍 Search URLs:',
        'search_placeholder': 'Enter search term...',
        'clear_filters': 'Clear Filters',
        'showing': 'Showing {current} of {total} stores',
        'no_data': 'No data matches the current filters',

        # Table Headers
        'url': 'URL',
        'status': 'Status',
        'last_check': 'Last Check',
        'first_dead_date': 'First Dead Date',
        'check_count': 'Check Count',
        'store_url': 'Store URL',
        'from': 'From',
        'to': 'To',
        'changed_at': 'Changed At',
        'change': 'Change',

        # Progress Messages
        'checking': '🔍 Checking {current}/{total}: {url}...',
        'rechecking_dead': '🔄 Rechecking DEAD store: {url}...',
        'completed_check': '✅ Completed checking {count} stores!',
        'rechecked_dead': '✅ Rechecked {count} DEAD stores!',
        'error_deleting': 'Error deleting: {error}',
    }
}


def get_text(key: str, lang: str = 'vi', **kwargs) -> str:
    """Get translated text for given key"""
    text = TRANSLATIONS.get(lang, TRANSLATIONS['vi']).get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text
