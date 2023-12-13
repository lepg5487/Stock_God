from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import sys
import requests
from bs4 import BeautifulSoup
import json
import re
import time
from selenium.webdriver.support.ui import Select
from fake_useragent import UserAgent


# 獲取執行檔案的路徑
exe_path = sys.argv[0]
script_directory = os.path.dirname(os.path.abspath(exe_path))
os.chdir(script_directory)

# --------------------------- 登入 ----------------------------
ua = UserAgent()
user1 = ua.random

login_header = {
    "User-Agent": user1
}

login_payload = {
    "form_type": "customer_login",
    "utf8": "✓",
    "customer[email]": "133221333123111@gmail.com",
    "customer[password]": "1234000",
    "return_url": "/account"
}

login_API = "https://nagano-market.jp/account/login"
# 使用 requests.session() 保持登入狀態, .session()包含cookies, 302的Header內容一樣無法取得.
login_session = requests.session()
login_response = login_session.post(login_API, headers=login_header, data=login_payload)
redirect_login_history = login_response.history
print(redirect_login_history) # 看重定向幾次

# --------- 取得商品ID----------
# https://nagano-market.jp/collections/20231006?page=1
# https://nagano-market.jp/collections/20231020?page=1
# https://nagano-market.jp/collections/20231213?page=1


date = "20231006"
first_page_url = f"https://nagano-market.jp/collections/{date}?page=1"
# 用户输入的商品名称 # 早上11:00慢1秒執行程式
target_product_names = ["マレーグマ", "もちきんちゃく"]

page_html_file = 'page_1.html'
# 发送HTTP请求获取第一个页面的HTML（仅在本地文件不存在时发送网络请求）
if not os.path.exists(page_html_file):
    # 发送HTTP请求获取第一个页面的HTML
    Webpage_header = {
        'User-Agent' : user1,
    }
    Webpage_response = requests.get(first_page_url, headers=Webpage_header)
    print(Webpage_response.status_code)

    if Webpage_response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(Webpage_response.text, 'html.parser')
        # 使用 find_all 选择所有具有 class="pagination--link" 的 <a> 元素
        pagination_links = soup.find_all('a', class_='pagination--link')
        # 获取最后一个元素的 page 值
        if pagination_links:
            last_page_value = pagination_links[-1]['href'].split('=')[-1]
            with open('total_page.txt', 'w') as file:
                file.write(last_page_value)
        else:
            last_page_value = None
        # 构建URL列表
        if last_page_value:
            urls_to_save = [f"https://nagano-market.jp/collections/{date}?page={i}"
            for i in range(1, int(last_page_value) + 1)]
        else:
        # 沒有pagination--link就是只有1頁
            urls_to_save = [first_page_url]
            with open('total_page.txt', 'w') as file:
                file.write("1")
        # 存储每个URL的HTML
        for i, url in enumerate(urls_to_save):
            response = requests.get(url)
            if response.status_code == 200:
                with open(f'page_{i + 1}.html', 'w', encoding='utf-8') as file:
                    file.write(response.text)
#                 print(f"Saved HTML from {url} to page_{i + 1}.html")
#             else:
#                 print(f"Failed to fetch HTML from {url}")
#     else:
#         print(f"Failed to fetch HTML from {first_page_url}")
# else:
#     print(f"Using local HTML file: {page_html_file}")

with open("total_page.txt", "r") as file:
    total_page = int(file.read())
print("總共頁數: ", total_page)

# 读取本地 HTML 文件
# with open("page_1.html", "r", encoding="utf-8") as file:
#     html_content = file.read()
page_number = 1
while True: 
    with open(f"page_{page_number}.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    # 使用正则表达式提取 var meta 的内容
    match = re.search(r'var meta = ({.*?});', html_content)
    if match:
        json_str = match.group(1)
        # 将 JSON 字符串转换为 Python 对象
        meta_data = json.loads(json_str)

        # 存储商品的列表
        products_info = []
        # 遍历每个产品，查找包含目标文字的商品
        for product in meta_data.get("products", []):
            for variant in product.get("variants", []):
                for target_product_name in target_product_names:
                    if target_product_name in variant.get("name", ""):
                        product_id = product.get("id")
                        variant_id = variant.get("id")
                        print(f"Product ID: {product_id}")
                        print(f"Variant ID: {variant_id}")
                        products_info.append({"product_id": product_id, "variant_id": variant_id})
                        #print(products_info)
                        break  # 找到匹配的商品后，结束当前循环
        if not products_info:
            print("")
        else:
            add_API = "https://nagano-market.jp/cart/add"
            cart_API = "https://nagano-market.jp/cart"

            # 构建 add_data 和 cart_data
            for product_info in products_info:
                add_data = {
                    "form_type": "product",
                    "utf8": "✓",
                    "id": product_info["variant_id"],
                    "quantity": "1",
                    "product-id": product_info["product_id"]
                }

                # 使用 POST 请求添加商品
                add_response = login_session.post(add_API, data=add_data)
                redirect_add_history = add_response.history
                print(redirect_add_history) # 看重定向幾次
                #print(add_data)

                # if add_response.ok:
                #     print(f"Product added successfully: {product_info['product_id']} - {product_info['variant_id']}")
                # else:
                #     print(f"Failed to add product: {product_info['product_id']} - {product_info['variant_id']}")

            print("總共商品數量: ", len(products_info))
            if len(products_info) == 1:
                cart_data = "updates%5B%5D=1&checkout="
            elif len(products_info) == 2:
                cart_data = "updates%5B%5D=1&updates%5B%5D=1&checkout="
            elif len(products_info) == 3:
                cart_data = "updates%5B%5D=1&updates%5B%5D=1&updates%5B%5D=1&checkout="
            elif len(products_info) == 4:
                cart_data = "updates%5B%5D=1&updates%5B%5D=1&updates%5B%5D=1&updates%5B%5D=1&checkout="    
            #print(cart_data)
            cart_response = login_session.post(cart_API, data=cart_data)
            redirect_cart_history = cart_response.history
            print(redirect_cart_history) # 看重定向幾次

            buy_url = redirect_cart_history[0].headers.get("Location")
            print(buy_url)

            # if cart_response.ok:
            #     print("Cart updated successfully.")
            # else:
            #     print("Failed to update cart.")

        page_number += 1
        if page_number > total_page:
            print("")
            break
    else:
        print("No match found for var meta.")

# # --------------------------- selenium ----------------------------

# 将Request的RequestsCookieJar格式的cookies转换为Selenium的cookies格式 dict
cookies_dict = requests.utils.dict_from_cookiejar(login_session.cookies)
#print(cookies_dict)

chrome_options = Options()
#options.chrome_executable_path="D:\nagano\chromedriver.exe"
#options.add_argument('--headless')  # 启用无头模式
#options.add_argument("--incognito")  # 使用無痕模式。
chrome_options.add_argument('--start-maximized')  # 最大化窗口，可根据需要调整
chrome_options.add_argument('user-agent='+user1)
driver = webdriver.Chrome(options=chrome_options)
driver.get(buy_url)

# -------- 接受所有cookies--------
shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zigzag-worldshopping-checkout'))).shadow_root

shadow_text = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zigzag-test__cookie-banner-accept-all')))
driver.execute_script("arguments[0].click();", shadow_text)

shadow_text1 = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zigzag-test__modal-close > img')))
driver.execute_script("arguments[0].click();", shadow_text1)

shadow_text2 = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zigzag-test__banner-deactivate')))
driver.execute_script("arguments[0].click();", shadow_text2)
# -------- 接受所有cookies--------

# -------- 進入購買頁面--------
# 将cookies_dict添加到Selenium的cookies中
for cookie_name, cookie_value in cookies_dict.items():
    driver.add_cookie({'name': cookie_name, 'value': cookie_value})

driver.get(buy_url)
# -------- 進入購買頁面--------
# -------- 排隊120s直到看到"配送先住所" --------
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Form0 > div:nth-child(1) > div > div > div.VheJw > div.s_qAq > div > section > div > h2')))
# dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Select0')))
# info_select = Select(dropdown)
# # 方法1：通过文本选择选项
# info_select.select_by_visible_text("新しい住所を使用する")
# -------- 排隊120s直到看到"配送先住所" --------
# -------- 情報 --------
info1 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TextField7')))
info1.clear()  # 清除文本框中的内容
info1.send_keys("林")
#driver.execute_script("arguments[0].value = arguments[1];", info1, "李")

info2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TextField8')))
info2.clear()  # 清除文本框中的内容
info2.send_keys("帥哥")
#driver.execute_script("arguments[0].value = arguments[1];", info2, "彥葦")

dropdown2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Select2')))
info_select2 = Select(dropdown2)
info_select2.select_by_visible_text("東京都")
info4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TextField10')))
info4.clear()  # 清除文本框中的内容
info4.send_keys("東京都足立区堀之内")
# driver.execute_script("arguments[0].value = arguments[1];", info4, "東京都足立区堀之内")

info5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TextField2')))
info5.clear()  # 清除文本框中的内容
info5.send_keys("1-1-23")
# driver.execute_script("arguments[0].value = arguments[1];", info5, "2-2-15")

info6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TextField3')))
info6.clear()  # 清除文本框中的内容
info6.send_keys("123, 123")
# driver.execute_script("arguments[0].value = arguments[1];", info6, "JpDeliver, JDZ0605842")

info7 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TextField6')))
info7.clear()  # 清除文本框中的内容
info7.send_keys("123-4567-8910")
# driver.execute_script("arguments[0].value = arguments[1];", info7, "050-5892-8605")

info3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#postalCode')))
#info3.clear()  # 清除文本框中的内容
info3.send_keys(Keys.CONTROL + "a")  # 选中所有文本
info3.send_keys(Keys.DELETE)  # 删除选中的文本
info3.send_keys("123-1234")
#driver.execute_script("arguments[0].value = arguments[1];", info3, "123-0874")

buy_element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Form0 > div:nth-child(1) > div > div > div.VheJw > div.oQEAZ > div > button')))
buy_element.click()
#driver.execute_script("arguments[0].click();", buy_element)
# -------- 情報 --------
# -------- 配送 --------
# -------- 等待120s直到看到"配送方法" --------
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#step-section-primary-header')))
buy_element2 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Form1 > div:nth-child(1) > div > div > div > div.oQEAZ > div:nth-child(1) > button')))
buy_element2.click()
#driver.execute_script("arguments[0].click();", buy_element2)
# -------- 配送 --------
# -------- 支払い --------
# -------- 等待120s直到看到"支払い" --------
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#step-section-primary-header')))
# 
# card-fields-number-b9hkktqoen700000-scope-nagano-market\.jp
# 部分匹配iframe的CSS_SELECTOR
# -----------------card -----------------
iframe_number = "[id^='card-fields-number-'][id$='-scope-nagano-market.jp']"
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, iframe_number)))
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#number')))
driver.execute_script("arguments[0].value = arguments[1];", input_element, "133221333123111")
# 切換回主頁面
driver.switch_to.default_content()

#card-fields-name-rtxg4ezusib00000-scope-nagano-market\.jp
# -----------------name -----------------
iframe_name = "[id^='card-fields-name-'][id$='-scope-nagano-market.jp']"
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, iframe_name)))
input_element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#name')))
driver.execute_script("arguments[0].value = arguments[1];", input_element2, "ji394su3")
driver.switch_to.default_content()

# #card-fields-expiry-sop817bcdls00000-scope-nagano-market\.jp
# -----------------expiry-----------------
iframe_expiry = "[id^='card-fields-expiry-'][id$='-scope-nagano-market.jp']"
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, iframe_expiry)))
input_element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#expiry')))
input_element3.send_keys("12")
input_element3.send_keys("34")
#driver.execute_script("arguments[0].value = arguments[1];", input_element3, "02")
driver.switch_to.default_content()

# #card-fields-verification_value-aurz9r9i8pj00000-scope-nagano-market\.jp
# -----------------verification_value-------------------
iframe_verification_value = "[id^='card-fields-verification_value-'][id$='-scope-nagano-market.jp']"
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, iframe_verification_value)))
input_element4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#verification_value')))
driver.execute_script("arguments[0].value = arguments[1];", input_element4, "123")
driver.switch_to.default_content()


# #Form2 > div:nth-child(1) > div > div.oQEAZ > div:nth-child(1) > div > button
# Finish = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Form2 > div:nth-child(1) > div > div.oQEAZ > div:nth-child(1) > div > button')))
# Finish.click()
# driver.execute_script("arguments[0].click();", Finish)


# -------- 支払い --------
#driver.quit()
input("按下任意鍵結束")

# # --------------------------- selenium ----------------------------
