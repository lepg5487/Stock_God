---
layout: testlayouts
---

# Music AI
[Magenta MT3](https://github.com/magenta/mt3) 產生 .MIDI檔, 再使用 [MuseScore](https://musescore.org/zh-hant) 產生爵士鼓譜 or 其他樂器譜  

# LM Studio
本地端大型語言模型(LLM)的應用程式，讓使用者能 下載、管理、運行 LLM，並透過 GUI 或 API 來與模型互動。  
像是可離線使用的 本地版 ChatGPT 並且支援多種開源模型。  
應用舉例, PotPlayer撥放器可以影片自動產生字幕並翻譯, 可以利用LM Studio自己在本地端架設LLM並開啟API Key,  
在PotPlayer設定連線API Key, 就能免費使用影片自動產生字幕並翻譯.  

# yolov5
應用舉例, 把楓之谷圖片標記(labels)想要辨識的"角色"或"怪物", 再利用yolov5機器學習訓模型(model), 在python載入模型torch.hub.load,  
取得yolov5圈起來的方框位置get_center(x1, y1, x2, y2), 再把角色位置player_pos和怪物位置firepig_pos互相靠近並攻擊.  
```
# 載入模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
model.conf = 0.5

# label mapping
LABELS = model.names
PLAYER_CLASS = 0
FIREPIG_CLASS = 1
FLOOR_CLASS = 2

def get_center(x1, y1, x2, y2):
    return int((x1 + x2) / 2), int((y1 + y2) / 2)

if cls == PLAYER_CLASS:
    player_pos = (cx, cy)
elif cls == FIREPIG_CLASS:
    firepig_pos = (cx, cy)
```

# AI Coding 介紹
```
AI Coding（AI 輔助程式開發）
   │
   └─ LLM Coding（底層核心技術：以大型語言模型為基礎）
          │
          ├─ 1. 底層大腦 (Models / 基礎模型)
          │      ├─ Codex (開山祖師，已退役)
          │      ├─ GPT-4o / Claude 3.7 / Gemini 3.1 Pro
          │      └─ DeepSeek Coder 等專門模型
          │
          └─ 2. 工作流與開發哲學 (使用方式)
                 │
                 ├─ A. 傳統 AI-Assisted (Copilot 模式 / 輔助型)
                 │      ├─ 特徵：單行/區塊代碼補全、右側聊天框問答、開發者手動整合
                 │      ├─ 主控權：開發者 (人類是駕駛，AI 是副駕)
                 │      └─ 代表工具：GitHub Copilot, Codeium, Amazon Q
                 │
                 └─ B. Vibe Coding (Agentic 模式 / 代理型)
                        ├─ 特徵：意圖導向、跨檔案大規模修改、自動跑終端機指令、自主除錯
                        ├─ 主控權：AI 代理 (AI 是執行團隊，人類是產品經理/審查員)
                        └─ 代表工具：Cursor (Composer), Google Antigravity, Devin, Windsurf
```

# n8n
開源的低程式碼自動化工作流工具, 熱門的自動化工具有 Zapier、Make、n8n.  
另外還有針對 AI、客服機器人、瀏覽器插件特化的自動化工具：Dify、Coze等等.  
有雲端和本地的版本，考量到許多工作流程需要放上私鑰（ex: Google API Key、OpenAI API Key），以及雲端版本至少要付費 20 歐元（限制工作流程執行 2500 次），所以選擇了本地部署的方案。  
[資料來源1](https://raymondhouch.com/lifehacker/digital-workflow/automation-tools-review/), [資料來源2](https://medium.com/dean-lin/n8n-%E6%95%99%E5%AD%B8-%E7%94%A8-docker-%E5%9C%A8-local-%E5%BB%BA%E7%AB%8B%E5%85%8D%E8%B2%BB-%E7%84%A1%E9%99%90%E6%AC%A1%E6%95%B8%E4%BD%BF%E7%94%A8%E7%9A%84%E8%87%AA%E5%8B%95%E5%8C%96%E5%B7%A5%E5%85%B7-ab603faa300f)  


