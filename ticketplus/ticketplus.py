import requests
from fake_useragent import UserAgent
import time
import json
import ddddocr
import cairosvg
import hashlib
import os
import re
import sys
import subprocess

# 獲取執行檔案的路徑
exe_path = sys.argv[0]
script_directory = os.path.dirname(os.path.abspath(exe_path))
os.chdir(script_directory)

# 使用完整路徑打開文件
info_path = os.path.join(script_directory, "info.txt")
with open(info_path) as f:
    content = f.read()

mymobile = re.search(r'mobile = "(.+)"', content).group(1) 
mypassword = re.search(r'password = "(.+)"', content).group(1)
mysessionId = re.search(r'sessionId = "(.+)"', content).group(1)
myproductId = re.search(r'productId = "(.+)"', content).group(1)
mycount = int(re.search(r'count = (\d+)', content).group(1))

def round_to_nearest_minute():
    current_time = time.time()
    rounded_time = round(current_time)
    return int(rounded_time - (rounded_time % 60))

# o t 有機率辨識錯誤
def run_ocr():
    ocr = ddddocr.DdddOcr(beta=True)
    with open("ORC.png", 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    return res

# script_directory = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_directory)
rounded_time = round_to_nearest_minute() * 1000

#---------------------------- 登入 --------------------------------
login_url = "https://api.ticketplus.com.tw/user/api/v1/login?_="+str(rounded_time)
print("login API =", login_url)
# 未加密的密码
password = mypassword
# 加密密码
hashed_password = hashlib.md5(password.encode()).hexdigest()

ua = UserAgent()
user1 = ua.random

print(user1)
#user1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
myheader={
    "User-Agent" : user1,
    "Referer" : "https://ticketplus.com.tw/",
    "Content-Type":"application/json"
}
mypayload = {
    "mobile": mymobile,
    "countryCode": "886",
    "password": hashed_password
}

mydata_json = json.dumps(mypayload)
read = requests.post(login_url, headers=myheader, data=mydata_json)
print("login API state =", read) # <Response [200]>
Response_login = read.json()
token = 'Bearer '+Response_login['userInfo']['access_token']

#---------------------------- 登入 --------------------------------




#---------------------------- 驗證碼 --------------------------------
# captcha API, generate?_=
url = "https://api.ticketplus.com.tw/captcha/api/v1/generate?_="+str(rounded_time)
print("captcha API =", url)

# Authorization token 60分鐘換一次 token, 10:30 -> 11:30 -> 12:30
myheader={
    "User-Agent" : user1,
    "Referer" : "https://ticketplus.com.tw/",
    "Authorization" : token
}
# print(myheader)
# json標準是雙引號, 一定要使用json.dumps
# data=payload, 每場sessionId不同
mydata={
    "sessionId":mysessionId
}
mydata_json = json.dumps(mydata)
#print(mydata) # {'sessionId': 's000000324'} 單引號伺服器吃不進去
#print(mydata_json) # {"sessionId": "s000000324"} 雙引號伺服器才能吃

read = requests.post(url, headers=myheader, data=mydata_json)
print("captcha API state =", read) # <Response [200]>
#print(read.json())
Response_Captcha = read.json()
#print(Response_Captcha["data"])
Response_Captcha_key = Response_Captcha["key"]
#print(Response_Captcha_key)
with open('ORC.svg', 'w') as f:
    f.write(Response_Captcha["data"])

# 将SVG文件转换为PNG 驗證碼
input_svg_file = 'ORC.svg'
output_png_file = 'ORC.png'
background_color = 'white'
cairosvg.svg2png(url=input_svg_file, write_to=output_png_file, background_color=background_color)
print("captcha =", run_ocr())
#---------------------------- 驗證碼 --------------------------------


# ------------------------- 訂票API -----------------------------------
# https://config.ticketplus.com.tw/config/api/v1/getS3?path=event/aa1bb348ddc09b68872066acfb70122f/products.json
# "productId": "p000002284", "productId": "p000002285", "productId": "p000002287"

# 訂票reserve API, reserve?_="
url2 = "https://api.ticketplus.com.tw/ticket/api/v1/reserve?_="+str(rounded_time)
print("reserve API =", url2)
myheader2={
    "User-Agent" : user1,
    "Referer" : "https://ticketplus.com.tw/",
    "Authorization" : token,
    "Content-Type":"application/json;charset=UTF-8"
}
mydata2={
    "products": [
        {
            "productId": myproductId,
            "count": mycount
        }
    ],
    "captcha": {
        "key": Response_Captcha_key,
        "ans": run_ocr()
    },
    "reserveSeats": True,
    "consecutiveSeats": True,
    "finalizedSeats": True
}

mydata_json2 = json.dumps(mydata2) # payload
print("reserve Header =", mydata_json2)

# while True:
#     read2 = requests.post(url2, headers=myheader2, data=mydata_json2)
#     print("reserve API state =", read2) # <Response [200]>
#     Response_Reserve = read2.json()
#     print(Response_Reserve['errCode'], Response_Reserve['errMsg'])

#     if Response_Reserve['errCode'] == '137':
#         print("繼續迴圈")
#     elif Response_Reserve['errCode'] == '00':
#         print("成功取得")
#         break
#     else:
#         # 不是 '137' 也不是 '00'，直接跳出迴圈
#         print("不是 '137'，跳出迴圈")
#         break

# input("整份程式結束, 按下Enter結束")
testexe = "ticketplus.exe"

while True:
    read2 = requests.post(url2, headers=myheader2, data=mydata_json2)
    print("reserve API state =", read2) # <Response [200]>
    Response_Reserve = read2.json()
    print(Response_Reserve['errCode'], Response_Reserve['errMsg'])

    if Response_Reserve['errCode'] == '137':
        print("繼續迴圈")
    elif Response_Reserve['errCode'] == '00':
        input("成功取得, 按下Enter結束")
        break
    elif Response_Reserve['errCode'] == '135':
        print("驗證碼錯誤重新執行整份程式")
        subprocess.call([testexe])
        break
    else:
        # 不是 '137' 也不是 '00' 也不是 '135'，直接跳出迴圈
        input("不是 '137'，跳出迴圈, 按下Enter結束")
        break

input("整份程式結束, 按下Enter結束")
# ------------------------- 訂票API -----------------------------------
