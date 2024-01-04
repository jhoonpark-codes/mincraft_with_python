from mcpi.minecraft import Minecraft
from javascript import require, On
import mcpi.block as block

# create mineflayer object by require
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

# connect to server 
HOST_SERVER = 'localhost'
BOT_USERNAME = 'jhoonpark-bot'
port = 4711
bot = mineflayer.createBot({ 'host': HOST_SERVER, 'port': port, 'username': BOT_USERNAME, 'hideErrors': False })


## server connection test
# original
mc = Minecraft.create()
mc.postToChat('Server Connected')


# get position
pos = mc.player.getPos()
direction = mc.player.getDirection()

## make chair
center = mc.player.getPos()

## clear area
mc.setBlocks(center.x - 50, 
             center.y, 
             center.z - 50, 
             center.x + 50, 
             center.y + 50, 
             center.z + 50,
             block.AIR)

## make floor
mc.setBlocks(center.x - 50, 
             center.y - 1, 
             center.z - 50, 
             center.x + 50, 
             center.y - 1, 
             center.z + 50,
             block.STONE)

APART_SIZE = 3
LEG_SIZE = 8
SEAT_SIZE = 8

# make wall
mc.setBlocks(center.x -50, 
             center.y, 
             center.z -50, 
             center.x -50, 
             center.y + 50, 
             center.z + 50,
             block.STONE)
mc.setBlocks(center.x - 50, 
             center.y, 
             center.z - 50, 
             center.x + 50, 
             center.y + 50, 
             center.z - 50,
             block.STONE)
mc.setBlocks(center.x + 50, 
             center.y, 
             center.z - 50, 
             center.x + 50, 
             center.y + 50, 
             center.z + 50,
             block.STONE)
mc.setBlocks(center.x - 50, 
             center.y, 
             center.z + 50, 
             center.x + 50, 
             center.y + 50, 
             center.z + 50,
             block.STONE)

#### 의자가 뒤로?
## make legs
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
             center.y, 
             center.z - APART_SIZE - SEAT_SIZE, 
             center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE, 
             center.z - APART_SIZE - SEAT_SIZE,
             block.WOOD)

mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
             center.y, 
             center.z - APART_SIZE, 
             center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE, 
             center.z - APART_SIZE, 
             block.WOOD)

mc.setBlocks(center.x - APART_SIZE, 
             center.y, 
             center.z - APART_SIZE - SEAT_SIZE, 
             center.x - APART_SIZE, 
             center.y + LEG_SIZE, 
             center.z - APART_SIZE - SEAT_SIZE, 
             block.WOOD)

mc.setBlocks(center.x - APART_SIZE, 
             center.y, 
             center.z - APART_SIZE, 
             center.x - APART_SIZE, 
             center.y + LEG_SIZE, 
             center.z - APART_SIZE, 
             block.WOOD)

# make seat
mc.setBlocks(center.x - APART_SIZE, 
             center.y + LEG_SIZE + 1, 
             center.z - APART_SIZE, 
             center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE + 1, 
             center.z - APART_SIZE - SEAT_SIZE, 
             block.WOOD)

# make back
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE   + 1, 
             center.z - APART_SIZE - SEAT_SIZE, 
             center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
             center.z - APART_SIZE - SEAT_SIZE, 
             block.WOOD)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE   + 1, 
             center.z - APART_SIZE, 
             center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
             center.z - APART_SIZE, 
             block.WOOD)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
             center.z - APART_SIZE , 
             center.x - APART_SIZE - SEAT_SIZE, 
             center.y + LEG_SIZE   + 1 + LEG_SIZE, 
             center.z - APART_SIZE - SEAT_SIZE, 
             block.WOOD)

### make cup
## under the chair
CUP_SIZE = 4

# Cup floor?
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.y, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
             center.y, 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
             block.IRON_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.y+1, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
             center.y+1, 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
             block.IRON_BLOCK)
# Cup wall?
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
             block.IRON_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
             block.IRON_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
             block.IRON_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
             block.IRON_BLOCK)
# Cup handle?
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3) , 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
             center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
             block.IRON_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3) - 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
             center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
             block.IRON_BLOCK)

## on the chair
CUP_SIZE = 4

# Cup floor?
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.y + LEG_SIZE + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
             center.y + LEG_SIZE + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
             block.GOLD_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.y + LEG_SIZE + 2 + 1, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
             center.y + LEG_SIZE + 2 + 1, 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
             block.GOLD_BLOCK)
# Cup wall?
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
             block.GOLD_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
             block.GOLD_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
             block.GOLD_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
             center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
             block.GOLD_BLOCK)
# Cup handle?
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3) , 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
             center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
             block.GOLD_BLOCK)
mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3) - 2, 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
             center.x - APART_SIZE - SEAT_SIZE//2, 
             center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
             center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
             block.GOLD_BLOCK)


##########################################
## 방향 설정 test
##########################################

## 23.12.31
## 1) connection 정의
## address = 'localhost'
## port = 4711 (default port)

from mcpi.connection import Connection
address, port = 'localhost', 4711 #### default setting
conn = Connection(address, port)

## 2) Minecraft object 생성
mc = Minecraft(conn)

## 2.1) object 생성 확인
## mc.create() X -> mc.player.setPos() working함 but why?
mc.player.getPos() # create  player위치 확인해줌



