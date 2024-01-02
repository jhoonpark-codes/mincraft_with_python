from mcpi.minecraft import Minecraft
from javascript import require, On
import mcpi.block as block

# create mineflayer object by require
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

# connect to server 
mc = Minecraft.create()
HOST_SERVER = 'localhost'
BOT_USERNAME = 'jhoonpark-bot'
bot = mineflayer.createBot({ 'host': HOST_SERVER, 'port': 25565, 'username': BOT_USERNAME, 'hideErrors': False })


# server connection test
mc.postToChat('Server Connected')

# get position
pos = mc.player.getPos()
direction = mc.player.getDirection()

## 아무것도 안 한 상태라면 
## direction.x = 0.32, direction.y = 0.11, direction.z = 0.93
## TODO : mc.player.setDirection(1,1,1) 확인

# make empty space
# referenced https://www.stuffaboutcode.com/2015/01/minecraft-api-players-direction.html

## make chair
center = mc.player.getPos()

## clear area
mc.setBlocks(center.x - 20, 
             center.y, 
             center.z - 20, 
             center.x + 20, 
             center.y + 20, 
             center.z + 20,
             block.AIR)

## make floor
mc.setBlocks(center.x - 20, 
             center.y - 1, 
             center.z - 20, 
             center.x + 20, 
             center.y - 1, 
             center.z + 20,
             block.STONE)

APART_SIZE = 3
LEG_SIZE = 4
SEAT_SIZE = 5
# make wall
mc.setBlocks(center.x -20, 
             center.y, 
             center.z -20, 
             center.x -20, 
             center.y + 20, 
             center.z + 20,
             block.WOOD)
mc.setBlocks(center.x - 20, 
             center.y, 
             center.z - 20, 
             center.x + 20, 
             center.y + 20, 
             center.z - 20,
             block.WOOD)
mc.setBlocks(center.x + 20, 
             center.y, 
             center.z - 20, 
             center.x + 20, 
             center.y + 20, 
             center.z + 20,
             block.WOOD)
mc.setBlocks(center.x - 20, 
             center.y, 
             center.z + 20, 
             center.x + 20, 
             center.y + 20, 
             center.z + 20,
             block.WOOD)

# make legs
mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE, 
             center.y, 
             center.z + APART_SIZE + SEAT_SIZE, 
             center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE, 
             center.z + APART_SIZE + SEAT_SIZE,
             block.WOOD)

mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE, 
             center.y, 
             center.z + APART_SIZE, 
             center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE, 
             center.z + APART_SIZE, 
             block.WOOD)

mc.setBlocks(center.x + APART_SIZE, 
             center.y, 
             center.z + APART_SIZE + SEAT_SIZE, 
             center.x + APART_SIZE, 
             center.y + LEG_SIZE, 
             center.z + APART_SIZE + SEAT_SIZE, 
             block.WOOD)

mc.setBlocks(center.x + APART_SIZE, 
             center.y, 
             center.z + APART_SIZE, 
             center.x + APART_SIZE, 
             center.y + LEG_SIZE, 
             center.z + APART_SIZE, 
             block.WOOD)

# make seat
mc.setBlocks(center.x + APART_SIZE, 
             center.y + LEG_SIZE + 1, 
             center.z + APART_SIZE, 
             center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE + 1, 
             center.z + APART_SIZE + SEAT_SIZE, 
             block.WOOD)

# make back
mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE   + 1, 
             center.z + APART_SIZE + SEAT_SIZE, 
             center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
             center.z + APART_SIZE + SEAT_SIZE, 
             block.WOOD)
mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE   + 1, 
             center.z + APART_SIZE, 
             center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
             center.z + APART_SIZE, 
             block.WOOD)
mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
             center.z + APART_SIZE , 
             center.x + APART_SIZE + SEAT_SIZE, 
             center.y + LEG_SIZE   + LEG_SIZE, 
             center.z + APART_SIZE + SEAT_SIZE, 
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
