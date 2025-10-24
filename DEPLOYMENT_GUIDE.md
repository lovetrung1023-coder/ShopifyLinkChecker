
# 📖 Hướng Dẫn Triển Khai / Deployment Guide

## 🇻🇳 Tiếng Việt

### 1. Chuẩn Bị

#### 1.1. Yêu Cầu Hệ Thống
- Python 3.11 trở lên
- PostgreSQL database
- Kết nối internet ổn định

#### 1.2. Dependencies
Dự án sử dụng các thư viện sau:
- `streamlit` - Framework web application
- `pandas` - Xử lý dữ liệu
- `plotly` - Visualization
- `psycopg2-binary` - PostgreSQL adapter
- `requests` - HTTP client

### 2. Triển Khai Trên Replit

#### 2.1. Import Dự Án
1. Đăng nhập vào [Replit](https://replit.com)
2. Click "Create Repl"
3. Chọn "Import from GitHub" hoặc upload source code
4. Chọn Python template

#### 2.2. Cấu Hình Database
1. Mở tab "Secrets" (biểu tượng khóa)
2. Thêm secret:
   ```
   Key: DATABASE_URL
   Value: postgresql://username:password@host:port/database
   ```

#### 2.3. Cấu Hình Telegram (Tùy Chọn)
1. Tạo bot qua [@BotFather](https://t.me/botfather)
2. Lấy Bot Token
3. Lấy Chat ID từ [@userinfobot](https://t.me/userinfobot)
4. Thêm vào Secrets:
   ```
   TELEGRAM_BOT_TOKEN: your_bot_token
   TELEGRAM_CHAT_ID: your_chat_id
   ```

#### 2.4. Khởi Chạy
1. Click nút "Run" ở đầu workspace
2. Ứng dụng sẽ chạy tại port 5000
3. Webview sẽ tự động mở

### 3. Triển Khai Production (Autoscale Deployment)

#### 3.1. Tạo Deployment
1. Click nút "Deploy" ở góc trên bên phải
2. Chọn "Autoscale" deployment type
3. Click "Set up your deployment"

#### 3.2. Cấu Hình
- **Machine Power**: Chọn dựa trên traffic dự kiến
  - Nhỏ (0.5 vCPU, 1GB RAM) - Cho traffic thấp
  - Trung bình (1 vCPU, 2GB RAM) - Cho traffic trung bình
  - Lớn (2 vCPU, 4GB RAM) - Cho traffic cao
- **Max instances**: Số lượng máy tối đa (khuyến nghị: 3-5)

#### 3.3. Deploy
1. Click "Deploy"
2. Đợi build hoàn thành
3. Deployment URL sẽ được cung cấp

### 4. Sử Dụng

#### 4.1. Load URLs
- **Upload File**: Upload file .txt chứa URLs (mỗi dòng 1 URL)
- **Manual Input**: Nhập URLs trực tiếp

#### 4.2. Kiểm Tra Stores
- Click "Start Checking All" để kiểm tra tất cả
- Click "Recheck DEAD Stores" để kiểm tra lại stores DEAD

#### 4.3. Lịch Tự Động
- Click "Start Scheduler" để bật kiểm tra tự động
- Thiết lập interval (phút)

#### 4.4. Đổi Giao Diện & Ngôn Ngữ
- Click nút "🌙 Tối" / "☀️ Sáng" để đổi theme
- Click nút "🇻🇳 VI" / "🇬🇧 EN" để đổi ngôn ngữ

### 5. Bảo Trì

#### 5.1. Backup Database
```bash
pg_dump $DATABASE_URL > backup.sql
```

#### 5.2. Xem Logs
- Trong Replit: Xem Console tab
- Trong Deployment: Click vào deployment > View logs

#### 5.3. Update Code
1. Commit changes trong Replit
2. Deployment sẽ tự động rebuild

### 6. Khắc Phục Sự Cố

#### 6.1. Ứng Dụng Không Chạy
- Kiểm tra DATABASE_URL đã được cấu hình
- Kiểm tra logs trong Console
- Restart deployment

#### 6.2. Telegram Không Hoạt Động
- Kiểm tra TELEGRAM_BOT_TOKEN và TELEGRAM_CHAT_ID
- Test connection trong app
- Kiểm tra bot có được start chưa

#### 6.3. Slow Performance
- Tăng machine power trong deployment
- Tăng max instances
- Check database connection

---

## 🇬🇧 English

### 1. Preparation

#### 1.1. System Requirements
- Python 3.11 or higher
- PostgreSQL database
- Stable internet connection

#### 1.2. Dependencies
The project uses the following libraries:
- `streamlit` - Web application framework
- `pandas` - Data processing
- `plotly` - Visualization
- `psycopg2-binary` - PostgreSQL adapter
- `requests` - HTTP client

### 2. Deployment on Replit

#### 2.1. Import Project
1. Login to [Replit](https://replit.com)
2. Click "Create Repl"
3. Select "Import from GitHub" or upload source code
4. Choose Python template

#### 2.2. Configure Database
1. Open "Secrets" tab (lock icon)
2. Add secret:
   ```
   Key: DATABASE_URL
   Value: postgresql://username:password@host:port/database
   ```

#### 2.3. Configure Telegram (Optional)
1. Create bot via [@BotFather](https://t.me/botfather)
2. Get Bot Token
3. Get Chat ID from [@userinfobot](https://t.me/userinfobot)
4. Add to Secrets:
   ```
   TELEGRAM_BOT_TOKEN: your_bot_token
   TELEGRAM_CHAT_ID: your_chat_id
   ```

#### 2.4. Run
1. Click "Run" button at the top of workspace
2. Application will run on port 5000
3. Webview will open automatically

### 3. Production Deployment (Autoscale)

#### 3.1. Create Deployment
1. Click "Deploy" button at top right
2. Select "Autoscale" deployment type
3. Click "Set up your deployment"

#### 3.2. Configuration
- **Machine Power**: Choose based on expected traffic
  - Small (0.5 vCPU, 1GB RAM) - For low traffic
  - Medium (1 vCPU, 2GB RAM) - For medium traffic
  - Large (2 vCPU, 4GB RAM) - For high traffic
- **Max instances**: Maximum number of machines (recommended: 3-5)

#### 3.3. Deploy
1. Click "Deploy"
2. Wait for build to complete
3. Deployment URL will be provided

### 4. Usage

#### 4.1. Load URLs
- **Upload File**: Upload .txt file with URLs (one per line)
- **Manual Input**: Enter URLs directly

#### 4.2. Check Stores
- Click "Start Checking All" to check all stores
- Click "Recheck DEAD Stores" to recheck DEAD stores

#### 4.3. Auto Scheduler
- Click "Start Scheduler" to enable auto-check
- Set interval (minutes)

#### 4.4. Change Theme & Language
- Click "🌙 Dark" / "☀️ Light" button to change theme
- Click "🇻🇳 VI" / "🇬🇧 EN" button to change language

### 5. Maintenance

#### 5.1. Backup Database
```bash
pg_dump $DATABASE_URL > backup.sql
```

#### 5.2. View Logs
- In Replit: Check Console tab
- In Deployment: Click deployment > View logs

#### 5.3. Update Code
1. Commit changes in Replit
2. Deployment will auto-rebuild

### 6. Troubleshooting

#### 6.1. Application Not Running
- Check DATABASE_URL is configured
- Check logs in Console
- Restart deployment

#### 6.2. Telegram Not Working
- Check TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID
- Test connection in app
- Check if bot is started

#### 6.3. Slow Performance
- Increase machine power in deployment
- Increase max instances
- Check database connection

---

## 📞 Support

For issues or questions:
- Check logs in Console
- Review this deployment guide
- Check Replit documentation: https://docs.replit.com

## 🔗 Useful Links

- [Replit Deployments](https://docs.replit.com/hosting/deployments/about-deployments)
- [Streamlit Documentation](https://docs.streamlit.io)
- [PostgreSQL on Replit](https://docs.replit.com/hosting/databases/postgresql)
