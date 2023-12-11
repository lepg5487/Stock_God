import requests
from bs4 import BeautifulSoup
import os
import sys
import json
from datetime import datetime
from urllib.parse import quote
import re

def generate_iso_timestamp():
    # 獲取當前的UTC時間
    current_utc_time = datetime.utcnow()
    # 格式化時間戳為 ISO 8601 標準
    iso_timestamp = current_utc_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    # 使用quote進行URL編碼
    url_encoded_timestamp = quote(iso_timestamp)
    return url_encoded_timestamp

# 獲取執行檔案的路徑
exe_path = sys.argv[0]
script_directory = os.path.dirname(os.path.abspath(exe_path))
os.chdir(script_directory)

# https://nagano-market.jp/collections/20231110?page=1
# --------------------------- 登入 ----------------------------

login_header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

login_payload = {
    "form_type": "customer_login",
    "utf8": "✓",
    "customer[email]": "siaotao0710@gmail.com",
    "customer[password]": "Momo0000",
    "return_url": "/account"
}

login_API = "https://nagano-market.jp/account/login"
# 使用 requests.session() 保持登入狀態, .session()包含cookies, 302的Header內容一樣無法取得.
login_session = requests.session()
login_response = login_session.post(login_API, headers=login_header, data=login_payload)

redirect_login_history = login_response.history
#HttpRequest中所带cookie和服务器端接收的cookie名称不一致，导致返回422错误代码。
print(redirect_login_history) # 看重定向幾次
#print(login_response.url)
print("")
print(redirect_login_history[0].headers)
print("")
print(redirect_login_history[0].headers.get("Location"))
print("")
print(redirect_login_history[0].headers.get("Set-Cookie"))
print("")
# ?需要_secure_session_id = 0690676d12fa79c49b8781c2fe4c17af
# ?需要secure_customer_sig = a89fbc62dcbd38c10923595292d9f9ef

# --------------------------- 登入 ----------------------------


# --------------------------- 購物車----------------------------
# multipart/form-data 不要設定Header, Content-Type: multipart/form-data
# add_header = {
#     # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
#     #"Cookie": ""
# }

# add_data_1 = {
#     "form_type": "product",
#     "utf8": "✓",
#     "id": "44099033399488",
#     "quantity": "1",
#     "product-id": "7601827610816"
# }

add_data_2 = {
    "form_type": "product",
    "utf8": "✓",
    "id": "44099033432256",
    "quantity": "1",
    "product-id": "7601827643584"
}

add_API = "https://nagano-market.jp/cart/add"
add_response_1 = login_session.post(add_API, data=add_data_2)
print(add_response_1.status_code)
print("")
redirect_add_history = add_response_1.history
print(redirect_add_history) # 看重定向幾次
print("")
print(redirect_add_history[0].headers)
print("")
print(redirect_add_history[0].headers.get("Location"))
print("")
print(redirect_add_history[0].headers.get("Set-Cookie"))
print("")

#? cart_sig = 2569754e10b0240bfa5da529906ff96c
# 只需要這個參數cart = c1-9e6f1f449c558795853877072ec144d9

set_cookie_header = redirect_add_history[0].headers.get("Set-Cookie")
# Define a regular expression pattern to match the cart cookie value
pattern = r"cart=([^;]+)"
# Use re.search to find the match in the Set-Cookie header
match = re.search(pattern, set_cookie_header)
# Check if a match is found and extract the cart cookie value
if match:
    cart_cookie_value = match.group(1)
    print("Cart Cookie Value:", cart_cookie_value)
else:
    print("Cart Cookie not found in Set-Cookie header")

# --------------------------- 購物車----------------------------

#https://nagano-market.jp/cart
# --------------------------- 結帳1 ----------------------------

cart_data = {
    "updates[]": "1",
    # "updates[]": "1",
    "checkout": ""
}

cart_API = "https://nagano-market.jp/cart" #add_response.url
cart_response = login_session.post(cart_API, data=cart_data)
redirect_cart_history = cart_response.history
print(redirect_cart_history) # 看重定向幾次
print("")
print(redirect_cart_history[0].headers)
print("")
print(redirect_cart_history[0].headers.get("Location"))
print("")
print(redirect_cart_history[0].headers.get("Set-Cookie"))
print("")

# # --------------------------- 結帳1 ----------------------------
