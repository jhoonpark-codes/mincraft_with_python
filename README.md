![image](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/10e6dcfb-b1b7-472b-bb83-a9c96cd03a23)
![image](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/4f4de2ab-d612-4e97-8f27-9a61df3e5997)
# minecraft_with_python
작성자 : 박정훈
> Python으로 Minecraft 조작하여 데이터셋 생성하기

## required list
- pytohn == 3.8
- java
- JDK
- MINECRAFT version 1.12
- MINECRACT server version 1.12
- mcpi (https://github.com/martinohanlon/mcpi)
- mineflayer (https://github.com/PrismarineJS/mineflayer/tree/master)

## Install
```shell
pip install javascript
pip install mcpi
pip install mineflayer
```

## Usage
**STEP 1. activate local server**
- Minecraft V1.12 implement 'server.js'

**STEP 2. create mcpi obj with create()**
```py
# mcpi
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
```

**STEP 3. import javascript and require mineflayer**
> **KEEP IN MIND**
* MineFlayer -> JavaScript로 구성
* Minecraft가 서버와 HTTP를 주고받으며 통신하기 때문에 Javascript로 쓰여진 MineFlayer의 명령어를 Python단에서 require을 통해 호출하는 방법으로 작동
```py
from javascript import require
mineflayer = require('mineflayer')
```

## 현재까지 진행 정도
* [print('Hello World') 예시 영상](https://drive.google.com/file/d/1meIPwxhEP05Z7XH0aJDPSr7Fid26Lbrg/view?usp=drive_link)
* [Block 만들기 예시 영상](https://drive.google.com/file/d/1qPSPauVqnphmSvWC2Zn6CxghRPFNQiPT/view?usp=drive_link)
* 의자 만들기 예시 1
![의자만든예시](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/6f772642-5059-491c-90fa-7ae6a8ea7c87)

* 의자 만들기 예시 2 - 항공샷
![의자항공샷](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/375bc0e7-3852-4a43-81a1-2bde315762e5)


## TODO

**MCPI API critical issues (23.12.20)**
* [방향 설정이 자유롭지 못함](https://www.stuffaboutcode.com/2015/01/minecraft-api-players-direction.html)
> "One of the questions I get asked a lot about the Minecraft: Pi edition APi is "how can I get the direction the player is facing?" and I have always had to say "sorry you can't do that"
* Block을 생성해서 의자, 책상을 만들어도 방향 설정이 자유롭지 않기 때문에 스크린캡처 시 올바른 방향 설정 불가능

**MineFlayer로 확장 중 (23.12.22)**
* MineFlayer API를 통해 bot을 생성하여 필요한 행동을 명령 내리는 형태로 진행 됨
```py
from javascript import require, once
mineflayer = require('mineflayer')

bot = mineflayer.createBot({ 'host': HOST, 'port': PORT_NO, 'username': BOT_USERNAME, 'hideErrors': False })

once(bot, 'login')
bot.chat('I Spawned')
```
- blockAt, can_see function : https://github.com/extremeheat/JSPyBridge/blob/master/examples/python/mineflayer2.py
- Functions : https://github.com/PrismarineJS/mineflayer/blob/master/docs/api.md
- Python example : https://github.com/PrismarineJS/mineflayer/tree/master/examples/python
