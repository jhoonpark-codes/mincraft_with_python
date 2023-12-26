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
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
```

**STEP 3. import javascript and require mineflayer**
> **KEEP IN MIND
* MineFlayer -> JavaScript로 구성
* Minecraft가 서버와 HTTP로 통신하기 때문에 Javascript로 쓰여진 MineFlayer의 명령어를 Python단에서 require을 통해 호출하는 방법으로 작동
```py
from javascript import require
mineflayer = require('mineflayer')
```

## TODO
### 현재 방향 설정이 자유롭지 못함 (https://www.stuffaboutcode.com/2015/01/minecraft-api-players-direction.html)
"One of the questions I get asked a lot about the Minecraft: Pi edition APi is "how can I get the direction the player is facing?" and I have always had to say "sorry you can't do that"
