---
layout: testlayouts
---

# LINE 貼圖製作過程
## 素材
[MapleStory風格](https://civitai.com/models/14313) + [MEMEAnyaHehFace](https://civitai.com/models/4391/lottalewds-anyahehface) 
MapleStory: prompt要放chibi, :[權重1到0.7] ,DPM++ 2M KARRAS 
MEMEAnyaHehFace: prompt要放huge shit-eating grin, wicked smug, and half closed eyes 
`prompt`
```
chibi, huge shit-eating grin, wicked smug, and half closed eyes
<lora:maplestoryStyle_v20:1> 
<lora:lottalewds_v0:1>
```
[TEXTUAL方式的EasyNegative](https://civitai.com/models/7808/easynegative)
`negative`
```
easynegative, 
```

------------------------------------------------------------------------------------------------------------------------------------------

## 約兒佛傑
#### 要
```
extremely detailed, finely detail, beautiful detailed eyes, masterpiece, best quality, extremely detailed cg unity 8k wallpaper, caustics, light smile, looking at viewer, 1girls, izakaya, full body, black hair, collarbone, off shoulder, small breasts, braid, shiny hair

```
#### 不要
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, simple background, low res, flat colors, bad feet, futa, missing arms, nsfw, pubic hair, foot
```
test: light persona(美化), hair up(頭髮盤起來),
kneeling, facing away,
covering breasts, covering crotch,
chibi

## 世界計畫 - 望月穗波
#### 要
```
extremely detailed, finely detail, beautiful detailed eyes, masterpiece, best quality, extremely detailed cg unity 8k wallpaper, caustics, light smile, looking at viewer, 1girls, full body, small breasts, shiny hair, bow, red bow, fingerless gloves, uniform, school uniform, collared shirt, buttons, light brown hair, low ponytail, smile, closed mouth, wide-eyed, tareme, blue eyes, drummer, bangs, red coat, drum, drum stick, cymbal
```
#### 不要
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, simple background, low res, flat colors, bad feet, futa, missing arms, nsfw, pubic hair, foot
```
![image](https://user-images.githubusercontent.com/26459046/199923282-173679e2-43f7-4f60-875b-2b6310f5d886.png)

## 世界計畫 - 宵崎奏
#### 要
```
extremely detailed, finely detail, beautiful detailed eyes, masterpiece, best quality, extremely detailed cg unity 8k wallpaper, caustics, light smile, looking at viewer, looking to the side, 1girls, full body, small breasts, shiny hair, smile, wide-eyed, tareme, blue eyes, t-shirt, white t-shirt, long hair, hair between eyes, silver hair, beret, pink beret, overalls
```
#### 不要
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, simple background, low res, flat colors, bad feet, futa, missing arms, nsfw, pubic hair, foot
```
![image](https://user-images.githubusercontent.com/26459046/199928089-5b193c34-17f4-47da-84ee-2c27e1cf6b6a.png)

## 喜多川海夢
#### 要
```
extremely detailed, finely detail, beautiful detailed eyes, masterpiece, best quality, extremely detailed cg unity 8k wallpaper, caustics, light smile, looking at viewer, gyaru, full body, medium breasts, shiny hair, smile, wide-eyed, tareme, blonde hair, gradient hair, parted bangs, collarbone, neck ring, uniform, collared shirt, necktie, blue necktie, pleated skirt, blue pleated skirt, hoop earrings, red eyes,
```
#### 不要
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, simple background, low res, flat colors, bad feet, futa, missing arms, nsfw, pubic hair, foot
```

## 瑪奇瑪
#### 要
```
extremely detailed, finely detail, beautiful detailed eyes, masterpiece, best quality, extremely detailed cg unity 8k wallpaper, caustics, light smile, looking at viewer, full body, medium breasts, shiny hair, bright pupils, smile, wide-eyed, tareme, collarbone, policewoman, red hair, braid, single braid, yellow eyes, spiral pupils, collared shirt, necktie
```
#### 不要
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, simple background, low res, flat colors, bad feet, futa, missing arms, nsfw, pubic hair, foot
```

## 帕瓦 パワー
#### 要
```
extremely detailed, finely detail, beautiful detailed eyes, masterpiece, best quality, extremely detailed cg unity 8k wallpaper, caustics, light smile, looking at viewer, full body, medium breasts, shiny hair, smile, wide-eyed, tareme, collarbone, blonde hair, parted bangs, yellow eyes, cross-shaped pupils, collared shirt, white collared shirt, necktie, black necktie, demon, red demon horns, coat
```
#### 不要
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, simple background, low res, flat colors, bad feet, futa, missing arms, nsfw, pubic hair, foot
```

## 參數
CFG Scale 這個可以簡單理解為AI對描述參數(tag)的傾向程度。

Denoising strength 則是可以簡單理解成原圖片的保留程度。

### 參考資料

[使用Google雲端:Colaboratory執行腳本](https://drive.google.com/file/d/1UONVm5mrhwZjT84Waw5MWCrCsGl9wUgw/view?usp=sharing)

[CFG Scale ,Denoising strength 解釋](https://zhuanlan.zhihu.com/p/574063064)

[標籤購物](https://tags.novelai.dev/)


#### 有衣服的 R18
```
collarbone, covered nipples, clothed sex, happy sex,
```

##### 主要改姿勢 擇1
```
girl on top, guided penetration
```
