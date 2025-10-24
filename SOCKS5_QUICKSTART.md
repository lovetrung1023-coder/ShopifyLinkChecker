# 🚀 Hướng Dẫn Nhanh: Dùng SOCKS5 Proxy (9proxy)

## ✅ Tính Năng Đã Thêm

Tool giờ hỗ trợ **SOCKS5 proxy** kèm **Manual Proxy Picker** - bạn có thể pick proxy trực tiếp trong giao diện!

## 📍 Vị Trí Manual Proxy Picker

Trong giao diện tool:
1. Mở sidebar bên trái
2. **Scroll xuống** đến section **"🌐 Cấu Hình Proxy"**
3. Bạn sẽ thấy:
   - Ô nhập: **"🎯 Chọn Proxy (Thủ Công)"**
   - Nút: **"✅ Áp Dụng Proxy"**
   - Nút: **"🔄 Xóa Proxy"**

## ⚡ Cách Dùng Với 9proxy (Nhanh Nhất)

### Bước 1: Expose 9proxy Ra Internet
Vì `127.0.0.1:60000` chỉ hoạt động local, bạn cần dùng **ngrok**:

```bash
# Chạy lệnh này trên máy của bạn (nơi 9proxy đang chạy)
ngrok tcp 60000
```

Ngrok sẽ cho bạn URL dạng:
```
tcp://0.tcp.ngrok.io:12345
```

### Bước 2: Nhập Vào Tool
1. Copy URL ngrok: `0.tcp.ngrok.io:12345`
2. Vào tool, mở sidebar
3. Scroll xuống phần **"🌐 Cấu Hình Proxy"**
4. Nhập vào ô proxy:
   ```
   socks5://0.tcp.ngrok.io:12345
   ```
5. Click **"✅ Áp Dụng Proxy"**
6. Thấy message: **"🎯 Đang dùng proxy thủ công: socks5://..."** → Thành công!

### Bước 3: Test
1. Upload vài links Shopify
2. Click **"Start Checking All"**
3. Tool sẽ check qua SOCKS5 proxy của bạn
4. IP được dùng = IP của 9proxy, không phải IP Việt Nam

## 📌 Các Định Dạng Proxy Hỗ Trợ

Tool hỗ trợ tất cả các loại proxy:

```bash
# SOCKS5 (không auth)
socks5://127.0.0.1:60000
socks5://0.tcp.ngrok.io:12345

# SOCKS5 (có auth)
socks5://username:password@proxy-host:1080

# HTTP/HTTPS
http://proxy.example.com:8080
https://user:pass@proxy.example.com:8080
```

## 🔄 Auto-Rotate vs Manual Pick

### Manual Pick (ưu tiên cao)
- Nhập proxy trong UI
- Áp dụng ngay lập tức
- **GHI ĐÈ** tất cả proxy khác

### Auto-Rotate (từ Secrets)
- Cấu hình trong Secrets: `PROXY_URL` hoặc `PROXY_LIST`
- Tự động xoay vòng
- Chỉ hoạt động khi **không có** manual proxy

**Để quay lại auto-rotate:** Click nút **"🔄 Xóa Proxy"**

## ⚠️ Lưu Ý Quan Trọng

### 1. Localhost Không Hoạt Động Trên Cloud
```
❌ SAI: socks5://127.0.0.1:60000
✅ ĐÚNG: socks5://0.tcp.ngrok.io:12345
```

Lý do: Replit chạy trên cloud server, không thể truy cập `127.0.0.1` trên máy bạn.

### 2. Ngrok Free Có Giới Hạn
- Ngrok free: 1 tunnel cùng lúc
- URL thay đổi mỗi lần restart ngrok
- Để fix: Dùng ngrok paid ($8/tháng) có fixed domain

### 3. Kiểm Tra Proxy Hoạt Động
Trước khi dùng trong tool, test proxy:
```bash
curl -x socks5://0.tcp.ngrok.io:12345 https://api.ipify.org
```

Phải trả về IP của proxy, không phải IP Việt Nam.

## 🆘 Troubleshooting

### Lỗi "Proxy Error"
**Nguyên nhân:** Proxy không kết nối được
**Giải pháp:**
1. Kiểm tra 9proxy có đang chạy không
2. Kiểm tra ngrok có đang chạy không
3. Test proxy bằng curl (lệnh ở trên)
4. Thử nhập lại URL proxy

### Không Thấy Proxy Picker
**Giải pháp:** Scroll xuống sidebar, phần proxy ở dưới cùng

### Proxy Chậm
**Nguyên nhân:** 
- Ngrok free có thể chậm
- 9proxy lag
**Giải pháp:**
- Tăng timeout (nếu cần)
- Kiểm tra kết nối internet

## 💡 Khuyến Nghị

### Cho Cá Nhân/Test
- Dùng 9proxy + ngrok (miễn phí)
- Pick proxy manual trong UI

### Cho Business/Production
- Mua proxy service (WebShare, Bright Data)
- Cấu hình nhiều proxy trong Secrets
- Để tool auto-rotate

## 📞 Cần Thêm Hỗ Trợ?

1. Đọc file **PROXY_SETUP.md** để biết chi tiết đầy đủ
2. Check logs trong Console tab nếu có lỗi
3. Test proxy trước khi dùng trong tool

---

**Tóm lại:**
1. Chạy: `ngrok tcp 60000`
2. Copy URL: `0.tcp.ngrok.io:xxxxx`
3. Nhập vào tool: `socks5://0.tcp.ngrok.io:xxxxx`
4. Click "Áp Dụng Proxy"
5. Done! ✅
