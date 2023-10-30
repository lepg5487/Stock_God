---
layout: testlayouts
---

#### 檢查網站需不需要重新整理 
`Ajax的最大優點，就是能在不更新整個頁面的前提下維護資料。`  
![image](https://github.com/lepg5487/Stock_God/assets/26459046/6f33d2b8-1d3e-4d79-b613-b170e5f1ce74)




---

# 建置過程
#### [安裝最新Node.js](https://nodejs.org/zh-tw/download)
```
cd Downloads/
tar -xf node-v18.18.2-linux-x64.tar.xz
sudo cp -r node-v18.18.2-linux-x64/* /usr/local/
sudo ln -s /usr/local/bin/node /usr/bin/node
sudo ln -s /usr/local/bin/npm /usr/bin/npm
```
##### 檢查是否安裝成功
```
npm -v
node -v
```
#### 建立Node.js伺服器
```
mkdir TicketTeleport
cd TicketTeleport
npm init
npm install express --save
vim app.js
node app.js
```

#### 建立React伺服器, react-app資料夾 (直接使用別人UI)
```
sudo npm install -g create-react-app
npx create-react-app react-app
cd react-app
npm start
```

#### [別人UIrepo](https://github.com/cornflourblue/react-redux-registration-login-example)
[錯誤解決](https://github.com/cornflourblue/react-redux-registration-login-example/issues/52)
```
git clone https://github.com/cornflourblue/react-redux-registration-login-example.git
cd react-redux-registration-login-example
npm audit fix --force
npm uninstall webpack webpack-cli webpack-dev-server -force
npm install webpack webpack-cli webpack-dev-server --save-dev
npm install
npm start
```
![image](https://github.com/lepg5487/Stock_God/assets/26459046/92395cdf-0875-4f0a-b8e1-a4be9277b732)

#### 安裝 Puppeteer 
`npm i puppeteer-core`  
##### 下載 [DeploySentinel Recorder](https://github.com/DeploySentinel/Recorder) 自動產生 Puppeteer script  
 
#### Step 1. [購票網頁tixcraft](https://tixcraft.com/activity)
#### Step 2. 確認網頁是登入且認證完成狀態

---


### [ORC開源解法](https://github.com/sml2h3/ddddocr)
#### Windows10 Bug 解決
module 'PIL.Image' has no attribute 'ANTIALIAS' -> `pip install Pillow==9.5.0`
#### [使用pyinstaller將.py打包成.exe (含ddddocr有bug)](https://zhuanlan.zhihu.com/p/456894600)
原本使用 `pyinstaller --onefile --noconsole --clean main.py` 編譯, 會出現缺少檔案.
![image](https://github.com/lepg5487/Stock_God/assets/26459046/5400c344-1e44-4695-9cbc-d6a30ac8f9d1)

修改 main.spec 檔案 `datas=[('./ddddocr/common.onnx','ddddocr')],`, 將檔案加入進去以後再編譯.
改用這指令 `pyinstaller main.spec` 編譯
![image](https://github.com/lepg5487/Stock_God/assets/26459046/e9b00430-bf19-4c50-a39e-35feb2b67d71)



---

# 訂閱制
step1: 輸入訂閱帳密  
step2: 同一時間訂閱帳密只能一個在線上 (如同時在線顯示:您的訂閱帳密在其他地方被登入,請盡快更改密碼)  
step3:  
[參考程式1](https://github.com/max32002/tixcraft_bot)
![image](https://github.com/lepg5487/Stock_God/assets/26459046/1d9bdfac-3047-40a4-b375-d6cda5e0a8da)

[參考程式2](https://www.youtube.com/watch?v=z-UwpsXY2Q4)
![image](https://github.com/lepg5487/Stock_God/assets/26459046/3507ff5a-8f1d-4956-b24d-3a88d514f6db)![image](https://github.com/lepg5487/Stock_God/assets/26459046/5811883d-7a02-4875-8ea6-a1e00be0c1f8)  

step4: 使用Google's OCR API自動辨識驗證碼(CAPTCHA)  
![image](https://github.com/lepg5487/Stock_God/assets/26459046/dddc3ab5-4f75-46d0-a588-40830d8bccb7)  

[Google's OCR API](https://dev.to/walrusai/using-google-s-ocr-api-with-puppeteer-for-visual-testing-42m6)  

[網路上也有很多人用機器學習訓練的開源專案](https://www.reddit.com/r/node/comments/bg3xr7/how_to_solve_simple_image_capcha_and_submit_it/)  

[google reCAPTCHA v3](https://www.google.com/recaptcha/api2/demo)

[法律注意](https://youtu.be/GTmZ8zd8xZo?t=395)
```
賣刀(程式), 沒叫你去殺人(買票).
不能"一步一步的教學".
```
