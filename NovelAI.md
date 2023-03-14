---
layout: testlayouts
---
# [NovelAI模組有四種載入的方式](https://github.com/civitai/civitai/wiki/How-to-use-models#textual-inversions)  
`Checkpoints`,`Textual `,`Hypernetwork`,`LoRA`.  

------------------------------------------------------------------------------------------------------------------------------------------

# LINE 貼圖製作過程2 (嘗試中)
## 素材

`prompt`
```
animalization, slimification, lineart, sketch

```
`negative`  
```
easynegative
```

------------------------------------------------------------------------------------------------------------------------------------------

# LINE 貼圖製作過程1 (被版權砲不能上架)
## 素材
[MapleStory風格](https://civitai.com/models/14313) + [MEMEAnyaHehFace](https://civitai.com/models/4391/lottalewds-anyahehface)  
[MapleStory2風格](https://civitai.com/models/8858/maplestory2game-style) + [MEMEAnyaHehFace](https://civitai.com/models/4391/lottalewds-anyahehface)  
MapleStory: prompt要放`chibi`, :[權重1到0.7] ,DPM++ 2M KARRAS  
MEMEAnyaHehFace: prompt要放`huge shit-eating grin`, `wicked smug`, `half closed eyes`  
[動畫素材(約兒)](https://civitai.com/models/5417/yor-forger-innocent-housewife-version-ti-embedding-by-corneo)  
約兒: prompt要放`black_hair`  
`prompt`
```
solo, chibi, huge shit-eating grin, wicked smug, half closed eyes,

corneo_yor_forger, black_hair,

<lora:maplestoryStyle_v20:1>
<lora:lottalewds_v0:1>
```
`negative`  
[TEXTUAL方式的EasyNegative](https://civitai.com/models/7808/easynegative)
```
easynegative
```
![Yor_AnyaHehFace](https://user-images.githubusercontent.com/26459046/224319634-c11bcf98-e94b-48ca-9bf5-e17d0e2d07c2.png)  

------------------------------------------------------------------------------------------------------------------------------------------

[動畫素材(海夢)](https://civitai.com/models/5251/corneos-marin-kitagawa-ti-embedding)  
海夢: prompt要放`school uniform`校服或`print bikini`比基尼.`earrings`耳環或`piercings`耳洞.`fake nails`假指甲或`long nails`長指甲等等  
`prompt`  
```
solo, chibi, huge shit-eating grin, wicked smug, half closed eyes,

corneo_marin_kitagawa, print bikini, earrings

<hypernet:maplestory2GameStyle_20:1> 
<lora:lottalewds_v0:1>
```
`negative`  
```
easynegative
```
![Marin_Kitagawa](https://user-images.githubusercontent.com/26459046/224457004-33a98442-f7c0-4d76-b28c-c57807ae3a75.png)

------------------------------------------------------------------------------------------------------------------------------------------

[動畫素材(Makima)](https://civitai.com/models/5331/corneos-makima-chainsaw-man-ti-embedding)  
Makima: prompt要放`white shirt`, `collared shirt`, `black necktie`, `black pants`, `ringed_eyes`
`prompt`  
```
solo, chibi, huge shit-eating grin, wicked smug, half closed eyes,

corneo_makima, white shirt, collared shirt, black necktie, black pants, ringed_eyes

<hypernet:maplestory2GameStyle_20:1>
<lora:lottalewds_v0:1>
```
`negative`  
```
easynegative
```
![Makima](https://user-images.githubusercontent.com/26459046/224466750-a7c7adb6-ecb1-414a-b32a-98fd4aef0e9e.png)

------------------------------------------------------------------------------------------------------------------------------------------

[動畫素材(Power)](https://civitai.com/models/5196/corneos-power-chainsaw-man-ti-embedding)  
Power: prompt要放`(sharp_teeth:0.8)`, `orange_eyes`
`prompt`  
```
solo, chibi, huge shit-eating grin, wicked smug, half closed eyes,

corneo_power, (sharp_teeth:0.8), orange_eyes

<hypernet:maplestory2GameStyle_20:1>
<lora:lottalewds_v0:1>
```
`negative`  
```
easynegative
```
![Power](https://user-images.githubusercontent.com/26459046/224466761-3e1be591-59a0-4c3b-9af6-10fb79dc341e.png)

------------------------------------------------------------------------------------------------------------------------------------------

[動畫素材(Kobeni)](https://civitai.com/models/6679/kobeni)  
Kobeni: prompt要放1girl, white shirt, black necktie, 3 hair clips, brown eyes,  
`prompt`  
```
solo, chibi, huge shit-eating grin, wicked smug, half closed eyes, 

1girl, white shirt, black necktie, 3 hair clips, brown eyes,

<hypernet:maplestory2GameStyle_20:1>
<lora:lottalewds_v0:1>
<lora:kobeni_v10:1>
```
`negative`  
```
easynegative
```
![Kobeni](https://user-images.githubusercontent.com/26459046/224466784-15f08cd7-eb9d-4ffe-909d-6e2e87618425.png)

------------------------------------------------------------------------------------------------------------------------------------------

[動畫素材nami](https://civitai.com/models/4219/one-piece-wano-style-lora)  
nami: prompt要放nami_1800,  
`prompt`  
```
solo, chibi, huge shit-eating grin, wicked smug

nami, wanostyle, straw hat, brown eyes,

<hypernet:maplestory2GameStyle_20:1>
<lora:lottalewds_v0:1>
<lora:onePieceWanoSagaStyle_v2Offset:0.5>
```
`negative`  
```
easynegative
```
![Nami](https://user-images.githubusercontent.com/26459046/224466792-34f3189e-0334-419f-96ff-0eaa70130d8f.png)

------------------------------------------------------------------------------------------------------------------------------------------

[動畫素材robin](https://civitai.com/models/4219/one-piece-wano-style-lora)  
robin: prompt要放robin_v2_3000  
`prompt`  
```
solo, chibi,  huge shit-eating grin, wicked smug

nico robin, wanostyle, blue_eyes, eyewear on head,  black long hair, high collar, hair slicked back, sea, wearing a blue jacket, neck is empty.

<hypernet:maplestory2GameStyle_20:1>
<lora:lottalewds_v0:1>
<lora:onePieceWanoSagaStyle_v2Offset:0.5>
```
`negative`  
```
easynegative
```
![nico_robin](https://user-images.githubusercontent.com/26459046/224466796-9725187d-e4a3-4299-944c-c6f368178892.png)

------------------------------------------------------------------------------------------------------------------------------------------

[動畫素材yamato](https://civitai.com/models/4219/one-piece-wano-style-lora)  
yamato: prompt要放yamato_5000  
`prompt`  
```
solo, chibi,  huge shit-eating grin, wicked smug

yamato, wanostyle, red horns,  white hair, green hair, gradient hair, kimono,  ring earrings, brown eyes,

<hypernet:maplestory2GameStyle_20:1>
<lora:lottalewds_v0:1>
<lora:onePieceWanoSagaStyle_v2Offset:0.5>
```
`negative`  
```
easynegative
```
![Yamato](https://user-images.githubusercontent.com/26459046/224466805-e9fda4fc-ea1f-4b52-a3c4-772d9ddcc660.png)

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
