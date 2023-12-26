from mcpi.minecraft import Minecraft
from javascript import require, On
import mcpi.block as block

# connect to server 
mc = Minecraft.create()

# create mineflayer object by require
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

# server connection test
mc.postToChat('Server Connected')

# get position
pos = mc.player.getPos()
direction = mc.player.getDirection()

## 아무것도 안 한 상태라면 
## direction.x = 0.32, direction.y = 0.11, direction.z = 0.93
## TODO : mc.player.setDirection(1,1,1) 확인

def make_space_for_objects(BLOCKDISTANCE, WALL_SIZE):
	pos = mc.player.getPos()
	
	# make empty space
	x_ = round(pos.x + (direction.x * BLOCKDISTANCE))
	y_ = round(pos.y + (direction.y * BLOCKDISTANCE) + 1)
	z_ = round(pos.z + (direction.z * BLOCKDISTANCE))	

	mc.setBlocks(pos.x, pos.y, pos.z, x_, y_, z_, block.AIR)

	# make stone floor
	mc.setBlocks(pos.x, pos.y, pos.z, x_, pos.y+1, z_, block.STONE)

	# make wall
	mc.setBlocks(pos.x, pos.y, z_, x_, pos.y+WALL_SIZE, z_, block.STONE)
	mc.setBlocks(x_, pos.y, pos.z, x_, pos.y+WALL_SIZE, z_, block.STONE)

	# move to center
	center_x = pos.x + (x_ - pos.x) // 2
	center_z = pos.z + (z_ - pos.z) // 2

	mc.player.setPos(center_x, pos.y+2, center_z)

	return x_, y_, z_, center_x, center_z


def make_chair(APART_SIZE, LEG_SIZE, SEAT_SIZE):
	## make chair
	center = mc.player.getPos()

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
	mc.setBlocks(center.x + APART_SIZE, 
	             center.y + LEG_SIZE   + LEG_SIZE//2, 
	             center.z + APART_SIZE + SEAT_SIZE, 
	             center.x + APART_SIZE + SEAT_SIZE, 
	             center.y + LEG_SIZE   + LEG_SIZE, 
	             center.z + APART_SIZE, 
	             block.WOOD)

def make_cup(SEAT_SIZE, CUBSIZE):

	## TODO
	## LOCATION argument 추가 필요
	## location : str in ['left', 'right', 'above', 'under']
	
	## make cup
	mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE//2, 
	             center.y + LEG_SIZE   + 2, 
	             center.z + APART_SIZE + SEAT_SIZE//2, 
	             center.x + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             center.y + LEG_SIZE   + 2, 
	             center.z + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             block.WOOD)
	mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE//2, 
	             center.y + LEG_SIZE   + 2 + CUPSIZE, 
	             center.z + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             center.x + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             center.y + LEG_SIZE   + 2 + CUPSIZE, 
	             center.z + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             block.WOOD)
	mc.setBlocks(center.x + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             center.y + LEG_SIZE   + 2 + CUPSIZE, 
	             center.z + APART_SIZE + SEAT_SIZE//2, 
	             center.x + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             center.y + LEG_SIZE   + 2 + CUPSIZE, 
	             center.z + APART_SIZE + SEAT_SIZE//2 + CUPSIZE, 
	             block.WOOD)	
