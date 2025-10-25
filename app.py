import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import os
import pytz
from utils.link_checker import ShopifyChecker
from utils.db_manager import DatabaseManager
from utils.export_manager import ExportManager
from utils.telegram_notifier import TelegramNotifier
from utils.scheduler import CheckScheduler
from utils.i18n import get_text

# Configure page
st.set_page_config(page_title="Shopify Store Monitor",
                   page_icon="🛍️",
                   layout="wide",
                   initial_sidebar_state="expanded")


def convert_utc_to_pacific(utc_timestamp_str):
    """Convert UTC ISO timestamp string to Pacific timezone string"""
    if not utc_timestamp_str or utc_timestamp_str in ['Never', '-', None]:
        return utc_timestamp_str
    
    try:
        pacific_tz = pytz.timezone('America/Los_Angeles')
        
        if isinstance(utc_timestamp_str, str):
            utc_dt = datetime.fromisoformat(utc_timestamp_str.replace('Z', '+00:00'))
        else:
            utc_dt = utc_timestamp_str
        
        if utc_dt.tzinfo is None:
            utc_dt = pytz.UTC.localize(utc_dt)
        
        pacific_dt = utc_dt.astimezone(pacific_tz)
        return pacific_dt.strftime('%Y-%m-%d %H:%M:%S %Z')
    except Exception as e:
        return utc_timestamp_str


def scheduled_check_callback():
    """Callback function for scheduled checks - runs in separate thread"""
    try:
        print("\n" + "="*50)
        print("🔄 SCHEDULED CHECK CALLBACK STARTED")
        print("="*50)
        
        # Create standalone instances for thread (can't use st.session_state in threads)
        print("📦 Creating instances...")
        data_manager = DatabaseManager()
        checker = ShopifyChecker()
        telegram_notifier = TelegramNotifier()
        
        # Get all stores
        data = data_manager.get_data()
        print(f"📊 Found {len(data)} stores to check")

        # Check each store
        for i, url in enumerate(data.keys(), 1):
            print(f"[{i}/{len(data)}] Checking: {url[:50]}...")
            status, timezone_checked = checker.check_store_status(url)

            # If DEAD, do second check
            if status == "DEAD":
                print(f"   ⚠️ DEAD detected, rechecking...")
                time.sleep(1)
                status, timezone_checked = checker.check_store_status(url)
                print(f"   Second check result: {status}")

            data_manager.update_store_status(url, status, timezone_checked)

        # Check for newly dead stores in the last 5 minutes
        print("\n🔍 Checking for newly dead stores (last 5 min)...")
        newly_dead = data_manager.get_newly_dead_stores(minutes=5)
        print(f"   Found {len(newly_dead)} newly dead stores")

        # Send Telegram notification if there are newly dead stores
        if newly_dead:
            print(f"📢 Attempting to notify about {len(newly_dead)} dead stores...")
            result = telegram_notifier.notify_dead_stores(newly_dead)
            print(f"   Notification result: {result}")
        else:
            print("   No newly dead stores to notify")

        # Also check for other status changes
        print("\n🔍 Checking for status changes (last 5 min)...")
        changes = data_manager.get_latest_changes(minutes=5)
        print(f"   Found {len(changes)} status changes")
        
        if changes:
            print(f"📢 Attempting to notify about {len(changes)} changes...")
            result = telegram_notifier.notify_status_changes(changes)
            print(f"   Notification result: {result}")
        else:
            print("   No status changes to notify")
        
        print("\n" + "="*50)
        print("✅ SCHEDULED CHECK CALLBACK COMPLETED")
        print("="*50 + "\n")

    except Exception as e:
        print(f"\n❌ ERROR in scheduled check: {e}")
        import traceback
        traceback.print_exc()


# Initialize session state
if 'data_manager' not in st.session_state:
    st.session_state.data_manager = DatabaseManager()
if 'checker' not in st.session_state:
    st.session_state.checker = ShopifyChecker()
if 'export_manager' not in st.session_state:
    st.session_state.export_manager = ExportManager()
if 'telegram_notifier' not in st.session_state:
    st.session_state.telegram_notifier = TelegramNotifier()
if 'scheduler' not in st.session_state:
    st.session_state.scheduler = CheckScheduler()
    st.session_state.scheduler.set_check_callback(scheduled_check_callback)
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'
if 'language' not in st.session_state:
    st.session_state.language = 'vi'


@st.cache_data(ttl=10, show_spinner=False)
def get_cached_status_counts():
    """Get cached status counts"""
    return st.session_state.data_manager.get_status_counts()


@st.cache_data(ttl=10, show_spinner=False)
def get_cached_counts():
    """Get cached total, live, dead, unpaid counts"""
    return {
        'total': st.session_state.data_manager.get_total_count(),
        'live': st.session_state.data_manager.get_live_count(),
        'dead': st.session_state.data_manager.get_dead_count(),
        'unpaid': st.session_state.data_manager.get_unpaid_count()
    }


def main():
    lang = st.session_state.language

    st.title(get_text('title', lang))
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.header(get_text('control_panel', lang))

        # Settings section at top
        st.subheader(get_text('settings', lang))

        col1, col2 = st.columns(2)
        with col1:
            if st.button('🇻🇳 VI' if st.session_state.language ==
                         'en' else '🇬🇧 EN'):
                st.session_state.language = 'en' if st.session_state.language == 'vi' else 'vi'
                st.rerun()

        st.markdown("---")

        # Input methods
        st.subheader(get_text('input_methods', lang))
        input_method = st.radio(
            get_text('choose_input', lang),
            [get_text('upload_file', lang),
             get_text('manual_input', lang)])

        # File upload
        if input_method == get_text('upload_file', lang):
            uploaded_file = st.file_uploader(get_text('choose_file', lang),
                                             type="txt",
                                             help=get_text('file_help', lang))

            if uploaded_file is not None:
                content = uploaded_file.getvalue().decode("utf-8")
                urls = [
                    line.strip() for line in content.splitlines()
                    if line.strip()
                ]
                st.info(get_text('file_contains', lang, count=len(urls)))

                if st.button(get_text('load_urls_file', lang)):
                    with st.spinner(
                            get_text('loading_urls', lang, count=len(urls))):
                        st.session_state.data_manager.load_urls(urls)
                    st.success(
                        get_text('loaded_success', lang, count=len(urls)))
                    st.rerun()

        # Manual input
        elif input_method == get_text('manual_input', lang):
            manual_urls = st.text_area(get_text('enter_urls', lang),
                                       height=150,
                                       help=get_text('enter_urls_help', lang))

            if st.button(get_text('load_manual', lang)):
                if manual_urls.strip():
                    urls = [
                        line.strip() for line in manual_urls.splitlines()
                        if line.strip()
                    ]
                    with st.spinner(
                            get_text('loading_urls', lang, count=len(urls))):
                        st.session_state.data_manager.load_urls(urls)
                    st.success(
                        get_text('loaded_success', lang, count=len(urls)))
                    st.rerun()

        st.markdown("---")

        # Check controls
        st.subheader(get_text('check_controls', lang))

        # Check all button
        if st.button(get_text('start_checking', lang), type="primary"):
            if st.session_state.data_manager.get_total_count() > 0:
                check_all_stores()
            else:
                st.error(get_text('no_urls', lang))

        # Quick recheck dead stores
        if st.button(get_text('recheck_dead', lang)):
            if st.session_state.data_manager.get_dead_count() > 0:
                recheck_dead_stores()
            else:
                st.info(get_text('no_dead', lang))

        st.markdown("---")

        # Scheduler controls
        st.subheader(get_text('scheduler', lang))

        scheduler_status = st.session_state.scheduler.get_status()

        col1, col2 = st.columns(2)
        with col1:
            if scheduler_status['running']:
                if st.button(get_text('stop_scheduler', lang)):
                    st.session_state.scheduler.stop()
                    st.rerun()
            else:
                if st.button(get_text('start_scheduler', lang)):
                    st.session_state.scheduler.start()
                    st.rerun()

        with col2:
            interval = st.number_input(
                get_text('interval', lang),
                min_value=5,
                max_value=1440,
                value=scheduler_status['interval_minutes'],
                step=5)
            if interval != scheduler_status['interval_minutes']:
                st.session_state.scheduler.set_interval(interval)

        if scheduler_status['running']:
            st.success(
                get_text('scheduler_running',
                         lang,
                         time=scheduler_status['next_check'][:19]
                         if scheduler_status['next_check'] else 'N/A'))
        else:
            st.info(get_text('scheduler_stopped', lang))

        st.markdown("---")

        # Telegram controls
        st.subheader(get_text('telegram', lang))

        if st.session_state.telegram_notifier.enabled:
            st.success(get_text('telegram_connected', lang))
            if st.button(get_text('test_telegram', lang)):
                if st.session_state.telegram_notifier.test_connection():
                    st.success(get_text('test_sent', lang))
                else:
                    st.error(get_text('test_failed', lang))
        else:
            st.warning(get_text('telegram_not_configured', lang))
            with st.expander(get_text('setup_instructions', lang)):
                st.markdown("""
                **To enable Telegram notifications:**

                1. Create a bot via [@BotFather](https://t.me/botfather)
                2. Get your bot token
                3. Get your chat ID from [@userinfobot](https://t.me/userinfobot)
                4. Set environment variables in Secrets:
                   - `TELEGRAM_BOT_TOKEN`
                   - `TELEGRAM_CHAT_ID`
                """)

        st.markdown("---")

        # Proxy configuration status
        st.subheader("🌐 Proxy Configuration" if lang == 'en' else "🌐 Cấu Hình Proxy")
        
        proxy_info = st.session_state.checker.get_proxy_info()
        
        # Manual proxy picker
        if 'manual_proxy_input' not in st.session_state:
            st.session_state.manual_proxy_input = ''
        
        manual_proxy_input = st.text_input(
            "🎯 " + ("Pick Proxy (Manual)" if lang == 'en' else "Chọn Proxy (Thủ Công)"),
            value=st.session_state.manual_proxy_input,
            placeholder="socks5://127.0.0.1:60000" if lang == 'vi' else "socks5://127.0.0.1:60000",
            help="HTTP, HTTPS, SOCKS5 supported. Example: socks5://127.0.0.1:60000" if lang == 'en' else "Hỗ trợ HTTP, HTTPS, SOCKS5. Ví dụ: socks5://127.0.0.1:60000",
            key="proxy_picker"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ " + ("Apply Proxy" if lang == 'en' else "Áp Dụng Proxy"), key="apply_proxy"):
                if manual_proxy_input.strip():
                    st.session_state.checker.set_manual_proxy(manual_proxy_input.strip())
                    st.session_state.manual_proxy_input = manual_proxy_input.strip()
                    st.success("✅ " + ("Proxy applied!" if lang == 'en' else "Đã áp dụng proxy!"))
                    st.rerun()
                else:
                    st.warning("⚠️ " + ("Please enter a proxy URL" if lang == 'en' else "Vui lòng nhập URL proxy"))
        
        with col2:
            if st.button("🔄 " + ("Clear Proxy" if lang == 'en' else "Xóa Proxy"), key="clear_proxy"):
                st.session_state.checker.set_manual_proxy(None)
                st.session_state.manual_proxy_input = ''
                st.success("✅ " + ("Proxy cleared!" if lang == 'en' else "Đã xóa proxy!"))
                st.rerun()
        
        # Show status
        if proxy_info['has_manual_proxy']:
            st.info(f"🎯 {'Using manual proxy' if lang == 'en' else 'Đang dùng proxy thủ công'}: `{proxy_info['manual_proxy']}`")
        elif proxy_info['enabled']:
            st.success(f"✅ {'Auto-rotating' if lang == 'en' else 'Tự động xoay'}: {proxy_info['total_proxies']} proxy")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Min Delay", f"{proxy_info['min_delay']}s")
            with col2:
                st.metric("Max Delay", f"{proxy_info['max_delay']}s")
        else:
            st.warning("⚠️ " + ("No proxy configured" if lang == 'en' else "Chưa cấu hình proxy"))
        
        st.markdown("---")
        
        # US Timezone Status
        st.subheader("🕐 US Timezone Status" if lang == 'en' else "🕐 Trạng Thái Múi Giờ US")
        
        tz_status = st.session_state.checker.get_us_timezone_status()
        
        if tz_status['smart_delay_enabled']:
            st.success("✅ " + ("Smart delay: Random US timezone mode" if lang == 'en' else "Smart delay: Chế độ random múi giờ US"))
            st.info("🎲 " + ("Each check randomly picks a US timezone for natural behavior" if lang == 'en' else "Mỗi lần check sẽ random 1 múi giờ US để giống người dùng thật"))
            
            # Show each timezone
            with st.expander("📍 " + ("View all US timezones" if lang == 'en' else "Xem tất cả múi giờ US")):
                for tz_name, info in tz_status['timezones'].items():
                    status_icon = "🔴" if info['is_peak_hours'] else "🟢" if info['is_off_hours'] else "🟡"
                    st.text(f"{status_icon} {tz_name}: {info['current_time']}")
        else:
            st.info("ℹ️ " + ("Smart delay disabled" if lang == 'en' else "Smart delay đang tắt"))
            with st.expander("📖 " + ("Setup Instructions" if lang == 'en' else "Hướng Dẫn Cấu Hình")):
                if lang == 'en':
                    st.markdown("""
                    **To enable proxy protection:**
                    
                    Add to your Secrets (environment variables):
                    
                    **Single proxy:**
                    - `PROXY_URL` = `http://username:password@proxy-ip:port`
                    
                    **Multiple proxies (auto-rotate):**
                    - `PROXY_LIST` = `http://user:pass@ip1:port,http://user:pass@ip2:port`
                    
                    **Optional delay settings:**
                    - `CHECK_MIN_DELAY` = `0.5` (minimum seconds between checks)
                    - `CHECK_MAX_DELAY` = `2.0` (maximum seconds between checks)
                    
                    **Example US proxy format:**
                    ```
                    PROXY_URL=http://username:password@us-proxy.example.com:8080
                    ```
                    """)
                else:
                    st.markdown("""
                    **Để bật bảo vệ proxy:**
                    
                    Thêm vào Secrets (biến môi trường):
                    
                    **Proxy đơn:**
                    - `PROXY_URL` = `http://username:password@proxy-ip:port`
                    
                    **Nhiều proxy (tự động xoay):**
                    - `PROXY_LIST` = `http://user:pass@ip1:port,http://user:pass@ip2:port`
                    
                    **Cài đặt delay (tùy chọn):**
                    - `CHECK_MIN_DELAY` = `0.5` (số giây tối thiểu giữa các lần check)
                    - `CHECK_MAX_DELAY` = `2.0` (số giây tối đa giữa các lần check)
                    
                    **Ví dụ định dạng proxy IP Mỹ:**
                    ```
                    PROXY_URL=http://username:password@us-proxy.example.com:8080
                    ```
                    
                    **Lưu ý:** Proxy IP Mỹ giúp ẩn IP thật của bạn khi check links.
                    """)

        st.markdown("---")

        # Export controls
        st.subheader(get_text('export_data', lang))
        export_options = [
            get_text('all_data', lang),
            get_text('live_only', lang),
            get_text('dead_only', lang),
            get_text('unpaid_only', lang)
        ]
        export_type = st.selectbox(get_text('export_type', lang),
                                   export_options)

        if st.button(get_text('download_export', lang)):
            export_data(export_type)

        st.markdown("---")

        # Delete controls
        st.subheader(get_text('delete_links', lang))

        with st.expander(get_text('delete_warning', lang)):
            st.warning(get_text('delete_warning', lang))

            delete_options = [
                get_text('select_option', lang),
                get_text('all_checked', lang),
                get_text('dead_links', lang),
                get_text('live_links', lang),
                get_text('unpaid_links', lang),
                get_text('unchecked_links', lang)
            ]
            delete_option = st.selectbox(get_text('choose_delete', lang),
                                         delete_options)

            if delete_option != get_text('select_option', lang):
                # Show count before deleting
                count_to_delete = 0
                if delete_option == get_text('all_checked', lang):
                    count_to_delete = st.session_state.data_manager.get_total_count(
                    ) - len(
                        st.session_state.data_manager.get_stores_by_status(
                            'UNCHECKED'))
                    st.info(
                        get_text('will_delete', lang, count=count_to_delete))
                elif delete_option == get_text('dead_links', lang):
                    count_to_delete = st.session_state.data_manager.get_dead_count(
                    )
                    st.info(
                        get_text('will_delete', lang, count=count_to_delete))
                elif delete_option == get_text('live_links', lang):
                    count_to_delete = st.session_state.data_manager.get_live_count(
                    )
                    st.info(
                        get_text('will_delete', lang, count=count_to_delete))
                elif delete_option == get_text('unpaid_links', lang):
                    count_to_delete = st.session_state.data_manager.get_unpaid_count(
                    )
                    st.info(
                        get_text('will_delete', lang, count=count_to_delete))
                elif delete_option == get_text('unchecked_links', lang):
                    count_to_delete = len(
                        st.session_state.data_manager.get_stores_by_status(
                            'UNCHECKED'))
                    st.info(
                        get_text('will_delete', lang, count=count_to_delete))

                if count_to_delete > 0:
                    confirm = st.checkbox(
                        get_text('confirm_delete', lang,
                                 count=count_to_delete))

                    if confirm and st.button(get_text('delete_now', lang),
                                             type="primary"):
                        with st.spinner(get_text('deleting', lang)):
                            deleted_count = delete_links_by_option(
                                delete_option)
                            get_cached_status_counts.clear()
                            get_cached_counts.clear()
                        st.success(
                            get_text('deleted_success',
                                     lang,
                                     count=deleted_count))
                        st.rerun()
                else:
                    st.info(get_text('no_links_delete', lang))

    # Main content area
    col1, col2, col3, col4 = st.columns(4)

    # Statistics cards (cached for performance)
    counts = get_cached_counts()
    total_count = counts['total']
    live_count = counts['live']
    dead_count = counts['dead']
    unpaid_count = counts['unpaid']

    with col1:
        st.metric(get_text('total_stores', lang), total_count)

    with col2:
        live_percentage = (live_count / total_count *
                           100) if total_count > 0 else 0
        st.metric(get_text('live_stores', lang), live_count,
                  f"{live_percentage:.1f}%")

    with col3:
        dead_percentage = (dead_count / total_count *
                           100) if total_count > 0 else 0
        st.metric(get_text('dead_stores', lang), dead_count,
                  f"{dead_percentage:.1f}%")

    with col4:
        unpaid_percentage = (unpaid_count / total_count *
                             100) if total_count > 0 else 0
        st.metric(get_text('unpaid_stores', lang), unpaid_count,
                  f"{unpaid_percentage:.1f}%")

    # Charts
    if total_count > 0:
        # Create tabs for different chart views
        tab1, tab2, tab3, tab4 = st.tabs([
            get_text('overview', lang),
            get_text('trends', lang),
            get_text('changes', lang),
            get_text('comparison', lang)
        ])

        with tab1:
            col1, col2 = st.columns(2)

            with col1:
                # Pie chart
                fig_pie = create_status_pie_chart()
                st.plotly_chart(fig_pie, use_container_width=True)

            with col2:
                # Bar chart for status distribution
                fig_bar = create_status_bar_chart()
                st.plotly_chart(fig_bar, use_container_width=True)

        with tab2:
            # Timeline trend analysis
            st.subheader(get_text('recent_changes', lang))

            col1, col2 = st.columns([3, 1])
            with col2:
                days_filter = st.selectbox(get_text('time_range', lang),
                                           [7, 14, 30, 60, 90],
                                           index=2,
                                           format_func=lambda x: get_text(
                                               'last_n_days', lang, days=x))

            # Fetch timeline data once with database-level filtering
            timeline_data = st.session_state.data_manager.get_timeline_data(
                days=days_filter)

            if timeline_data:
                # Stacked area chart for status over time
                fig_area = create_stacked_area_chart_from_data(
                    timeline_data, days_filter)
                st.plotly_chart(fig_area, use_container_width=True)

                # Line chart for individual status trends
                fig_line = create_status_trend_lines_from_data(
                    timeline_data, days_filter)
                st.plotly_chart(fig_line, use_container_width=True)
            else:
                st.info(get_text('no_timeline_data', lang, days=days_filter))

        with tab3:
            # Status changes analysis
            st.subheader(get_text('recent_changes', lang))

            days_range = st.slider(get_text('show_changes', lang), 1, 30, 7)
            changes = st.session_state.data_manager.get_status_changes(
                days_range)

            if changes:
                display_status_changes(changes)
            else:
                st.info(get_text('no_changes', lang, days=days_range))

        with tab4:
            # Comparison and analysis
            st.subheader(get_text('check_comparison', lang))

            col1, col2 = st.columns(2)

            with col1:
                comparison_options = [
                    get_text('last_hour', lang),
                    get_text('last_6_hours', lang),
                    get_text('last_24_hours', lang),
                    get_text('last_7_days', lang)
                ]
                comparison_period = st.selectbox(get_text(
                    'compare_over', lang),
                                                 comparison_options,
                                                 index=2)

            period_map = {
                get_text('last_hour', lang): 60,
                get_text('last_6_hours', lang): 360,
                get_text('last_24_hours', lang): 1440,
                get_text('last_7_days', lang): 10080
            }

            minutes = period_map[comparison_period]
            comparison_changes = st.session_state.data_manager.get_latest_changes(
                minutes)

            if comparison_changes:
                st.markdown(
                    f"### {get_text('changes_in', lang, period=comparison_period)}"
                )

                # Summary metrics
                col1, col2, col3 = st.columns(3)

                with col1:
                    newly_dead_count = len([
                        c for c in comparison_changes
                        if c['to_status'] == 'DEAD'
                    ])
                    st.metric(
                        get_text('newly_dead', lang),
                        newly_dead_count,
                        delta=-newly_dead_count if newly_dead_count > 0 else 0,
                        delta_color="inverse")

                with col2:
                    recovered_count = len([
                        c for c in comparison_changes if
                        c['to_status'] == 'LIVE' and c['from_status'] == 'DEAD'
                    ])
                    st.metric(
                        get_text('recovered', lang),
                        recovered_count,
                        delta=recovered_count if recovered_count > 0 else 0)

                with col3:
                    total_changes = len(comparison_changes)
                    st.metric(get_text('total_changes', lang), total_changes)

                # Detailed changes table
                display_status_changes(comparison_changes)

                # Send notification button
                if st.button(get_text('send_summary', lang)):
                    if st.session_state.telegram_notifier.notify_status_changes(
                            comparison_changes):
                        st.success(get_text('summary_sent', lang))
                    else:
                        st.error(get_text('summary_failed', lang))
            else:
                st.info(
                    get_text('no_changes_period',
                             lang,
                             period=comparison_period.lower()))

    # Filters and search
    st.markdown("---")
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        status_filter = st.multiselect(
            get_text('filter_status',
                     lang), ["LIVE", "DEAD", "UNPAID", "UNCHECKED"],
            default=["LIVE", "DEAD", "UNPAID", "UNCHECKED"])

    with col2:
        search_term = st.text_input(get_text('search_urls', lang),
                                    placeholder=get_text(
                                        'search_placeholder', lang))

    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(get_text('clear_filters', lang)):
            st.rerun()

    # Data table
    display_data_table(status_filter, search_term)


def check_all_stores():
    """Check all stores with progress tracking"""
    lang = st.session_state.language
    data = st.session_state.data_manager.get_data()
    total_urls = len(data)

    if total_urls == 0:
        st.error(get_text('no_urls', lang))
        return

    progress_container = st.container()

    with progress_container:
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i, (url, store_data) in enumerate(data.items()):
            progress = (i + 1) / total_urls
            progress_bar.progress(progress)
            status_text.text(
                get_text('checking',
                         lang,
                         current=i + 1,
                         total=total_urls,
                         url=url[:50]))

            status, timezone_checked = st.session_state.checker.check_store_status(url)

            if status == "DEAD":
                status_text.text(
                    get_text('rechecking_dead', lang, url=url[:50]))
                time.sleep(1)
                status, timezone_checked = st.session_state.checker.check_store_status(url)

            st.session_state.data_manager.update_store_status(url, status, timezone_checked)

        progress_bar.empty()
        status_text.empty()

    newly_dead = st.session_state.data_manager.get_newly_dead_stores(minutes=5)
    if newly_dead:
        st.session_state.telegram_notifier.notify_dead_stores(newly_dead)

    changes = st.session_state.data_manager.get_latest_changes(minutes=5)
    if changes:
        st.session_state.telegram_notifier.notify_status_changes(changes)

    get_cached_status_counts.clear()
    get_cached_counts.clear()

    st.success(get_text('completed_check', lang, count=total_urls))
    st.rerun()


def recheck_dead_stores():
    """Recheck only DEAD stores"""
    lang = st.session_state.language
    dead_stores = st.session_state.data_manager.get_stores_by_status("DEAD")

    if not dead_stores:
        st.info(get_text('no_dead', lang))
        return

    progress_container = st.container()

    with progress_container:
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i, url in enumerate(dead_stores):
            progress = (i + 1) / len(dead_stores)
            progress_bar.progress(progress)
            status_text.text(get_text('rechecking_dead', lang, url=url[:50]))

            status, timezone_checked = st.session_state.checker.check_store_status(url)
            st.session_state.data_manager.update_store_status(url, status, timezone_checked)

        progress_bar.empty()
        status_text.empty()

    get_cached_status_counts.clear()
    get_cached_counts.clear()

    st.success(get_text('rechecked_dead', lang, count=len(dead_stores)))
    st.rerun()


def create_status_pie_chart():
    """Create pie chart for status distribution"""
    data = get_cached_status_counts()

    colors = {
        'LIVE': '#28a745',
        'DEAD': '#dc3545',
        'UNPAID': '#ffc107',
        'UNCHECKED': '#6c757d'
    }

    fig = go.Figure(data=[
        go.Pie(labels=list(data.keys()),
               values=list(data.values()),
               hole=.3,
               marker_colors=[
                   colors.get(status, '#6c757d') for status in data.keys()
               ])
    ])

    fig.update_layout(title=get_text('status_distribution',
                                     st.session_state.language),
                      annotations=[
                          dict(text=get_text('status',
                                             st.session_state.language),
                               x=0.5,
                               y=0.5,
                               font_size=20,
                               showarrow=False)
                      ])

    return fig


def create_status_bar_chart():
    """Create bar chart for status distribution"""
    data = get_cached_status_counts()

    colors = {
        'LIVE': '#28a745',
        'DEAD': '#dc3545',
        'UNPAID': '#ffc107',
        'UNCHECKED': '#6c757d'
    }

    fig = go.Figure(data=[
        go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            marker_color=[
                colors.get(status, '#6c757d') for status in data.keys()
            ],
            text=list(data.values()),
            textposition='auto',
        )
    ])

    fig.update_layout(title=get_text('status_distribution',
                                     st.session_state.language),
                      xaxis_title=get_text('status',
                                           st.session_state.language),
                      yaxis_title="Number of Stores",
                      showlegend=False)

    return fig


def create_stacked_area_chart_from_data(timeline_data: list, days: int = 30):
    """Create stacked area chart from pre-fetched timeline data"""
    lang = st.session_state.language
    df = pd.DataFrame(timeline_data)
    df['date'] = pd.to_datetime(df['date'])

    if df.empty:
        fig = go.Figure()
        fig.add_annotation(text=get_text('no_timeline_data', lang, days=days),
                           xref="paper",
                           yref="paper",
                           x=0.5,
                           y=0.5,
                           showarrow=False)
        fig.update_layout(
            title=get_text('status_composition', lang, days=days))
        return fig

    df_pivot = df.pivot_table(index='date',
                              columns='status',
                              values='count',
                              fill_value=0)

    colors = {
        'LIVE': '#28a745',
        'DEAD': '#dc3545',
        'UNPAID': '#ffc107',
        'UNCHECKED': '#6c757d'
    }

    fig = go.Figure()

    for status in df_pivot.columns:
        fig.add_trace(
            go.Scatter(x=df_pivot.index,
                       y=df_pivot[status],
                       name=status,
                       mode='lines',
                       stackgroup='one',
                       fillcolor=colors.get(status, '#6c757d'),
                       line=dict(width=0.5,
                                 color=colors.get(status, '#6c757d'))))

    fig.update_layout(title=get_text('status_composition', lang, days=days),
                      xaxis_title="Date",
                      yaxis_title="Number of Checks",
                      hovermode='x unified')

    return fig


def create_status_trend_lines_from_data(timeline_data: list, days: int = 30):
    """Create line chart from pre-fetched timeline data"""
    lang = st.session_state.language
    df = pd.DataFrame(timeline_data)
    df['date'] = pd.to_datetime(df['date'])

    if df.empty:
        fig = go.Figure()
        fig.add_annotation(text=get_text('no_timeline_data', lang, days=days),
                           xref="paper",
                           yref="paper",
                           x=0.5,
                           y=0.5,
                           showarrow=False)
        fig.update_layout(title=get_text('status_trends', lang, days=days))
        return fig

    colors = {
        'LIVE': '#28a745',
        'DEAD': '#dc3545',
        'UNPAID': '#ffc107',
        'UNCHECKED': '#6c757d'
    }

    fig = px.line(df,
                  x='date',
                  y='count',
                  color='status',
                  title=get_text('status_trends', lang, days=days),
                  labels={
                      'count': 'Number of Checks',
                      'date': 'Date'
                  },
                  color_discrete_map=colors)

    fig.update_layout(hovermode='x unified')
    fig.update_traces(mode='lines+markers')

    return fig


def display_status_changes(changes):
    """Display status changes in a formatted table"""
    lang = st.session_state.language
    df_changes = pd.DataFrame(changes)

    df_changes['changed_at'] = df_changes['changed_at'].apply(convert_utc_to_pacific)

    df_changes = df_changes.rename(
        columns={
            'url': get_text('store_url', lang),
            'from_status': get_text('from', lang),
            'to_status': get_text('to', lang),
            'changed_at': get_text('changed_at', lang)
        })

    def create_change_indicator(row):
        from_status = row[get_text('from', lang)]
        to_status = row[get_text('to', lang)]

        status_colors = {
            'LIVE': '🟢',
            'DEAD': '🔴',
            'UNPAID': '🟡',
            'UNCHECKED': '⚪'
        }

        return f"{status_colors.get(from_status, '⚪')} {from_status} → {status_colors.get(to_status, '⚪')} {to_status}"

    df_changes[get_text('change',
                        lang)] = df_changes.apply(create_change_indicator,
                                                  axis=1)

    df_changes = df_changes[[
        get_text('store_url', lang),
        get_text('change', lang),
        get_text('changed_at', lang)
    ]]

    st.dataframe(df_changes, use_container_width=True, hide_index=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        newly_dead = len([c for c in changes if c['to_status'] == 'DEAD'])
        st.metric(get_text('newly_dead', lang),
                  newly_dead,
                  delta=-newly_dead if newly_dead > 0 else 0,
                  delta_color="inverse")

    with col2:
        recovered = len([
            c for c in changes
            if c['from_status'] == 'DEAD' and c['to_status'] == 'LIVE'
        ])
        st.metric(get_text('recovered', lang),
                  recovered,
                  delta=recovered if recovered > 0 else 0)

    with col3:
        total_changes = len(changes)
        st.metric(get_text('total_changes', lang), total_changes)


def display_data_table(status_filter, search_term):
    """Display filtered data table"""
    lang = st.session_state.language
    filtered_data = st.session_state.data_manager.get_filtered_data(
        status_filter, search_term)

    if not filtered_data:
        st.info(get_text('no_data', lang))
        return

    df_data = []
    for url, data in filtered_data.items():
        timezone_display = data.get('timezone_checked', '-')
        if timezone_display and timezone_display != '-':
            # Rút gọn tên múi giờ
            timezone_display = timezone_display.split('/')[-1]
        
        df_data.append({
            get_text('url', lang):
            url,
            get_text('status', lang):
            data.get('status', 'UNCHECKED'),
            'Timezone' if lang == 'en' else 'Múi Giờ':
            timezone_display,
            get_text('last_check', lang):
            convert_utc_to_pacific(data.get('last_check', 'Never')),
            get_text('first_dead_date', lang):
            convert_utc_to_pacific(data.get('first_dead_date', '-')),
            get_text('check_count', lang):
            data.get('check_count', 0)
        })

    df = pd.DataFrame(df_data)

    def style_status(val):
        colors = {
            'LIVE': 'background-color: #d4edda; color: #155724',
            'DEAD': 'background-color: #f8d7da; color: #721c24',
            'UNPAID': 'background-color: #fff3cd; color: #856404',
            'UNCHECKED': 'background-color: #e2e3e5; color: #383d41'
        }
        return colors.get(val, '')

    styled_df = df.style.map(style_status, subset=[get_text('status', lang)])
    st.dataframe(styled_df, use_container_width=True)

    st.info(
        get_text('showing',
                 lang,
                 current=len(df),
                 total=st.session_state.data_manager.get_total_count()))


def delete_links_by_option(delete_option):
    """Delete links based on selected option (optimized with bulk delete)"""
    lang = st.session_state.language
    try:
        if delete_option == get_text('all_checked', lang):
            statuses_to_delete = ['LIVE', 'DEAD', 'UNPAID']
            deleted = st.session_state.data_manager.bulk_delete_by_status(
                statuses_to_delete)
        elif delete_option == get_text('dead_links', lang):
            deleted = st.session_state.data_manager.bulk_delete_by_status(
                ['DEAD'])
        elif delete_option == get_text('live_links', lang):
            deleted = st.session_state.data_manager.bulk_delete_by_status(
                ['LIVE'])
        elif delete_option == get_text('unpaid_links', lang):
            deleted = st.session_state.data_manager.bulk_delete_by_status(
                ['UNPAID'])
        elif delete_option == get_text('unchecked_links', lang):
            deleted = st.session_state.data_manager.bulk_delete_by_status(
                ['UNCHECKED'])
        return deleted
    except Exception as e:
        st.error(get_text('error_deleting', lang, error=str(e)))
        return 0


def export_data(export_type):
    """Handle data export"""
    lang = st.session_state.language
    with st.spinner(get_text('exporting', lang)):
        # Map display names to internal names
        type_map = {
            get_text('all_data', lang): 'All Data',
            get_text('live_only', lang): 'LIVE Only',
            get_text('dead_only', lang): 'DEAD Only',
            get_text('unpaid_only', lang): 'UNPAID Only'
        }
        internal_type = type_map.get(export_type, export_type)

        filename = st.session_state.export_manager.export_data(
            st.session_state.data_manager, internal_type)

        if filename:
            with open(filename, 'r') as f:
                st.download_button(label=f"📥 {export_type}",
                                   data=f.read(),
                                   file_name=os.path.basename(filename),
                                   mime='text/plain')
            st.success(get_text('export_success', lang, type=export_type))


if __name__ == "__main__":
    main()
