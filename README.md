![image](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/10e6dcfb-b1b7-472b-bb83-a9c96cd03a23)
![image](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/4f4de2ab-d612-4e97-8f27-9a61df3e5997)
![image](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/cf9aa628-05c5-4c74-a4e5-a8fd9c57edd5)
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
- pillow
- opencv-python
- numpy
- mineflayer (https://github.com/PrismarineJS/mineflayer/tree/master)
- AIMStarterKitPC 다운

## Install
```shell
pip install javascript
pip install mcpi
pip install mineflayer
```

## Usage
**STEP 1. activate local server**
- Minecraft V1.12 implement 'server.js'

**STEP 2. create mcpi obj with create() (23.12.31 수정)**
```py
# mcpi
from mcpi.minecraft import Minecraft
from mcpi.connection import Connection
import mcpi.block as block

address, port = 'localhost', 4711
conn = Connection(address, port)

mc = Minecraft(conn).create()
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
* 실내 공간 / 의자 / 컵 완성
![image](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/dac40d33-eabe-4d0d-9567-3e29d8059ebc)
* Scale-up Test DONE ! (24.01.16)
> [Scale-up test demo video](https://drive.google.com/drive/folders/1szzehm-Nq9RHP4AU2UJbyzd4R2hNiM-8)


## HISTORY

**MCPI API critical issues (23.12.20)**
* [방향 설정이 자유롭지 못함](https://www.stuffaboutcode.com/2015/01/minecraft-api-players-direction.html)
> "One of the questions I get asked a lot about the Minecraft: Pi edition APi is "how can I get the direction the player is facing?" and I have always had to say "sorry you can't do that"
* Block을 생성해서 의자, 책상을 만들어도 방향 설정이 자유롭지 않기 때문에 스크린캡처 시 올바른 방향 설정 불가능

**MineFlayer로 확장 중 (23.12.22)**
* MineFlayer API를 통해 bot을 생성하여 필요한 행동을 명령 내리는 형태로 진행 됨
* MineFlayer 실행 시 참고할 점
> Node.js 설치해야 함 (https://nodejs.org/en)
> third party plugin도 있음 (https://github.com/PrismarineJS/mineflayer#third-party-plugins)

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

* 중간결론
- MineFlayer은 bot을 만들어서 액션하게 하는 모듈
- bot으로 block은 생성할 수 있으나 봇의 시야에서 스크린을 캡처할 수 없음
- 결국 mcpi와 마찬가지로 시야 및 방향에서 문제가 생김
- (24.01.03 Update) 99% 자동화까진 가능할 것으로 보임


**Picraft 도입 검토 중 (23.12.31)**
* mcpi와 비슷한 Picraft 라이브러리 사용 가능
* mcpi와 비슷한 기능을 하나 mcpi에선 안 되는 기능들이 다수 존재
> 참조 사이트 : https://picraft.readthedocs.io/en/release-1.0/install.html

**치명적 결함 (24.01.01)**
* 캡쳐할 때 망치나 칼 같은 플레이어의 도구가 보임
![image](https://github.com/jhoonpark-codes/mincraft_with_python/assets/154233920/dac40d33-eabe-4d0d-9567-3e29d8059ebc)
* (수정(24.01.03)) IJCAI 2019 논문엔 그냥 툴 보이게 데이터 구성하긴 함 (https://www.ijcai.org/proceedings/2019/0339.pdf)




**기존 Minecraft 서버에 로그인 되지 않을 때 해결법 (24.01.06)**
* 현상 : 이미 사용중인 이름이라는 메세지와 함께 기존 계정으로 로그인 할 수 없으며 Microsoft 계정에 MineCraft가 없다는 메세지가 뜨며 에러 발생
* 해결 1 : Minecraft 홈페이지에서 Microsoft 계정으로 로그인
* 해결 2 : 런처 재다운로드
* 완료
> 이거 때문에 갑자기 안 되는 줄 알고 많이 쫄았다.

**SCALE-UP test DONE! (24.01.16 updated)**
* main.py
* block -> 벽 : block.STONE 의자 : block.WOOD 컵 : block.GOLD_ORE
* 10회 반복 생성에 걸리는 시간 3초 미만
* screenshot : PIL.ImageGrab, cv2.cvtColor, cv2.imshow, cv2.waitkey, cv2.imwrite
* screenshot 생성 완료
* random.random으로 의자의 위/아래/좌/우를 랜덤하게 선택하여 스크린 캡처 완료
> DONE(24.01.16):
> 1) 만들고 -> 찍고 -> 지우고 -> 다시 만들고 자동화
> TODO
> 1) 의자, 컵이 이쁘진 않긴 함


