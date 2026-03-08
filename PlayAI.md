---
layout: testlayouts
---

# Music AI
[Magenta MT3](https://github.com/magenta/mt3) 產生 .MIDI檔, 再使用 [MuseScore](https://musescore.org/zh-hant) 產生爵士鼓譜 or 其他樂器譜  

# LM Studio
本地端大型語言模型(LLM)的應用程式，讓使用者能 下載、管理、運行 LLM，並透過 GUI 或 API 來與模型互動。 像是可離線使用的 本地版 ChatGPT 並且支援多種開源模型。  
應用舉例, PotPlayer撥放器可以影片自動產生字幕並翻譯, 可以利用LM Studio自己在本地端架設LLM並開啟API Key, 在PotPlayer設定連線API Key, 就能免費使用影片自動產生字幕並翻譯.  

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
