# Hướng Dẫn Cấu Hình Proxy IP Mỹ (HTTP/HTTPS/SOCKS5)

## ✨ Tính Năng Mới: Hỗ Trợ SOCKS5 + Manual Proxy Picker

Tool giờ hỗ trợ:
- ✅ **HTTP/HTTPS Proxy**
- ✅ **SOCKS5 Proxy** (mới!)
- ✅ **Manual Proxy Picker** - Chọn proxy trực tiếp trong UI
- ✅ **Auto-rotation** - Tự động xoay nhiều proxy

## ⚠️ LƯU Ý QUAN TRỌNG VỀ LOCALHOST (127.0.0.1)

Nếu bạn đang dùng proxy trên **máy local** (127.0.0.1:60000), proxy đó **KHÔNG THỂ hoạt động** khi deploy trên Replit/Render vì:
- Replit/Render chạy trên server cloud
- `127.0.0.1` trên server cloud khác với `127.0.0.1` trên máy bạn

**Giải pháp:**

### Cách 1: Expose Proxy Ra Public Internet (Khuyến nghị cho 9proxy)
Dùng **ngrok** hoặc **cloudflared** để forward port 60000:

```bash
# Dùng ngrok
ngrok tcp 60000

# Hoặc cloudflared
cloudflared tunnel --url tcp://localhost:60000
```

Sau đó lấy URL public và dùng trong tool. Ví dụ:
```
socks5://0.tcp.ngrok.io:12345
```

### Cách 2: Dùng IP Public của 9proxy
Nếu 9proxy hỗ trợ remote connection, lấy IP public và port:
```
socks5://your-public-ip:60000
```

### Cách 3: Chạy 9proxy Trên Replit (Nâng cao)
Upload 9proxy lên Replit và chạy background. Sau đó dùng `127.0.0.1:60000` (chỉ hoạt động trong Replit).

## Tại Sao Cần Dùng Proxy?

Khi bạn triển khai tool này trên Render hoặc Replit, các request check links sẽ đi từ IP của server (thường là ở Mỹ hoặc châu Âu). Tuy nhiên, nếu check quá nhiều store trong thời gian ngắn, Shopify có thể:
- Phát hiện pattern và rate limit
- Block IP của server tạm thời
- Đánh dấu các request là bot

**Proxy giúp:**
- Rotate IP giữa nhiều địa chỉ khác nhau
- Tránh bị phát hiện pattern
- Tăng tính ẩn danh khi check links
- Bảo vệ IP server của bạn

## Cách Cấu Hình Proxy

### 1. Lấy Thông Tin Proxy IP Mỹ

Bạn có thể mua proxy IP Mỹ từ các dịch vụ như:
- **Bright Data** (trước đây là Luminati) - https://brightdata.com
- **Oxylabs** - https://oxylabs.io
- **Smartproxy** - https://smartproxy.com
- **ProxyMesh** - https://proxymesh.com
- **WebShare** - https://www.webshare.io

**Định dạng proxy thường là:**
```
http://username:password@proxy-server:port
```

hoặc với HTTPS:
```
https://username:password@proxy-server:port
```

### 2. Cấu Hình Trên Replit

#### Bước 1: Mở Secrets
1. Click vào biểu tượng **khóa** (🔒) ở sidebar bên trái
2. Hoặc vào **Tools** > **Secrets**

#### Bước 2: Thêm Proxy

**Cách 1: Sử dụng 1 proxy**
```
Key: PROXY_URL
Value: http://username:password@us-proxy.example.com:8080
```

**Cách 2: Sử dụng nhiều proxy (tự động xoay - khuyến nghị)**
```
Key: PROXY_LIST
Value: http://user1:pass1@proxy1.com:8080,http://user2:pass2@proxy2.com:8080,http://user3:pass3@proxy3.com:8080
```

**Lưu ý:** Nhiều proxy giúp rotate IP hiệu quả hơn. Mỗi lần check, tool sẽ tự động chọn proxy khác nhau.

#### Bước 3: Cấu Hình Delay (Tùy Chọn)

Để tránh bị phát hiện, thêm random delay giữa các lần check:

```
Key: CHECK_MIN_DELAY
Value: 0.5

Key: CHECK_MAX_DELAY
Value: 2.0
```

Có nghĩa là mỗi lần check sẽ delay random từ 0.5 - 2.0 giây.

### 3. Cấu Hình Trên Render

#### Bước 1: Vào Dashboard
1. Mở project của bạn trên Render
2. Click vào **Environment**

#### Bước 2: Thêm Environment Variables

Click **Add Environment Variable** và thêm:

```
PROXY_URL = http://username:password@us-proxy.example.com:8080
```

hoặc với nhiều proxy:

```
PROXY_LIST = http://user1:pass1@proxy1.com:8080,http://user2:pass2@proxy2.com:8080
```

#### Bước 3: Deploy lại
Click **Manual Deploy** > **Deploy latest commit** để áp dụng thay đổi.

## Ví Dụ Cụ Thể

### Ví dụ 1: WebShare Proxy (Giá rẻ - $2.99/tháng cho 10 proxy)

```
PROXY_LIST = http://username-country-us:password@p.webshare.io:80,http://username-country-us-session-abc123:password@p.webshare.io:80
```

### Ví dụ 2: Bright Data

```
PROXY_URL = http://customer-USERNAME-cc-us:PASSWORD@brd.superproxy.io:33335
```

### Ví dụ 3: Smartproxy

```
PROXY_LIST = http://user123:pass456@us.smartproxy.com:10000,http://user123:pass456@us.smartproxy.com:10001
```

### Ví dụ 4: SOCKS5 Proxy (9proxy qua ngrok)

```
PROXY_URL = socks5://0.tcp.ngrok.io:12345
```

### Ví dụ 5: SOCKS5 với Authentication

```
PROXY_URL = socks5://username:password@proxy-host:1080
```

## 🎯 Cách Dùng Manual Proxy Picker

Trong giao diện tool, bạn sẽ thấy section **"🌐 Cấu Hình Proxy"** với:

1. **Ô nhập proxy**: Nhập URL proxy trực tiếp
   - Ví dụ: `socks5://127.0.0.1:60000` (nếu chạy local)
   - Ví dụ: `socks5://0.tcp.ngrok.io:12345` (qua ngrok)
   - Ví dụ: `http://user:pass@proxy.com:8080`

2. **Nút "Áp Dụng Proxy"**: Click để áp dụng proxy vừa nhập

3. **Nút "Xóa Proxy"**: Xóa proxy thủ công và quay về auto-rotate (nếu có)

**Lưu ý:** Manual proxy sẽ ghi đè tất cả proxy trong Secrets. Để quay lại auto-rotate, nhấn "Xóa Proxy".

## Kiểm Tra Proxy Đã Hoạt Động

1. Sau khi thêm proxy vào Secrets, restart ứng dụng
2. Vào sidebar bên trái, tìm section **"🌐 Cấu Hình Proxy"**
3. Nếu thấy:
   - ✅ **Proxy đang bật: X proxy** → Thành công!
   - ⚠️ **Proxy chưa cấu hình** → Kiểm tra lại secrets

## Smart Delay (Tránh Phát Hiện Bởi Shopify)

Tool có tính năng **Smart Delay** tự động điều chỉnh tốc độ check dựa trên múi giờ US:

### Cách Hoạt Động:
- **Giờ cao điểm** (9am-5pm ở nhiều bang US): Delay x2.5 (chậm hơn để tránh phát hiện)
- **Giờ làm việc** (8am-10pm): Delay x1.5 (vừa phải)
- **Ngoài giờ cao điểm**: Delay x1.0 (tốc độ bình thường)

### Cấu Hình:
```env
USE_SMART_DELAY=true          # Bật smart delay (mặc định: true)
CHECK_MIN_DELAY=0.5           # Delay tối thiểu (giây)
CHECK_MAX_DELAY=2.0           # Delay tối đa (giây)
```

### Tắt Smart Delay:
Nếu bạn muốn tốc độ tối đa (không khuyến khích):
```env
USE_SMART_DELAY=false
```

## Các Lỗi Thường Gặp

### Lỗi 1: "Proxy Error" khi check
**Nguyên nhân:** Proxy không hoạt động hoặc sai thông tin đăng nhập
**Giải pháp:** 
- Kiểm tra lại username/password
- Test proxy bằng curl: `curl -x http://user:pass@proxy:port https://google.com`

### Lỗi 2: Vẫn check bằng IP server
**Nguyên nhân:** Format proxy sai
**Giải pháp:** Đảm bảo format đúng: `http://username:password@host:port`

### Lỗi 3: Tool chạy chậm hơn
**Nguyên nhân:** Smart delay đang bật trong giờ cao điểm US
**Giải pháp:** 
- Check ngoài giờ cao điểm (sau 10pm hoặc trước 8am US time)
- Hoặc tắt smart delay (không khuyến khích): `USE_SMART_DELAY=false`

### Lỗi 4: Bị Shopify block
**Nguyên nhân:** Check quá nhanh, không dùng proxy hoặc proxy kém
**Giải pháp:**
- Bật smart delay: `USE_SMART_DELAY=true`
- Dùng proxy US chất lượng cao
- Tăng delay: `CHECK_MIN_DELAY=1.0` và `CHECK_MAX_DELAY=3.0`

## Bảo Mật

⚠️ **QUAN TRỌNG:**
- Không bao giờ share thông tin proxy công khai
- Không commit proxy credentials vào Git
- Chỉ lưu proxy trong Secrets/Environment Variables
- Thay đổi password proxy định kỳ

## Chi Phí Ước Tính

### Proxy Giá Rẻ (Shared/Residential):
- **WebShare**: $2.99/tháng cho 10 proxy US
- **ProxyMesh**: $10/tháng cho 10 proxy US
- **Smartproxy**: $12.5/tháng cho 5GB bandwidth

### Proxy Chất Lượng Cao (Residential/ISP):
- **Bright Data**: $15/tháng (pay as you go)
- **Oxylabs**: $20/tháng (shared pool)

### Khuyến Nghị:
- **Cho cá nhân/test:** WebShare (rẻ nhất)
- **Cho business:** Bright Data hoặc Oxylabs (ổn định hơn)

## Lưu Ý Về Shopify

Shopify có thể phát hiện bot dựa trên:
1. **Request rate:** Quá nhiều request/giây từ cùng IP
2. **Pattern:** Check cùng lúc nhiều store khác nhau
3. **User-Agent:** Header không giống browser thật

Tool này đã có:
- ✅ Random delay giữa các request
- ✅ User-Agent giả lập Chrome
- ✅ Proxy rotation (nếu bạn cấu hình)

**Khuyến nghị sử dụng:**
- Tối đa 3-5 proxy xoay vòng
- Delay 0.5-2 giây giữa các lần check
- Không check quá 100 stores cùng lúc

## Hỗ Trợ

Nếu gặp vấn đề, kiểm tra:
1. Format proxy có đúng không
2. Proxy có hoạt động không (test với curl)
3. Username/password có chính xác không
4. Secrets đã được lưu và app đã restart chưa
