from mcpi.minecraft import Minecraft
from javascript import require, On
import mcpi.block as block


def make_space_for_objects(center, SIZE = 50):
	## clear area
	mc.setBlocks(center.x - SIZE, 
	             center.y, 
	             center.z - SIZE, 
	             center.x + SIZE, 
	             center.y + SIZE, 
	             center.z + SIZE,
	             block.AIR)
	
	## make floor
	mc.setBlocks(center.x - SIZE, 
	             center.y - SIZE, 
	             center.z - SIZE, 
	             center.x + SIZE, 
	             center.y - SIZE, 
	             center.z + SIZE,
	             block.STONE)
	# make wall
	mc.setBlocks(center.x -SIZE, 
	             center.y, 
	             center.z -SIZE, 
	             center.x -SIZE, 
	             center.y + SIZE, 
	             center.z + SIZE,
	             block.STONE)
	mc.setBlocks(center.x - SIZE, 
	             center.y, 
	             center.z - SIZE, 
	             center.x + SIZE, 
	             center.y + SIZE, 
	             center.z - SIZE,
	             block.STONE)
	mc.setBlocks(center.x + SIZE, 
	             center.y, 
	             center.z - SIZE, 
	             center.x + SIZE, 
	             center.y + SIZE, 
	             center.z + SIZE,
	             block.STONE)
	mc.setBlocks(center.x - SIZE, 
	             center.y, 
	             center.z + SIZE, 
	             center.x + SIZE, 
	             center.y + SIZE, 
	             center.z + SIZE,
	             block.STONE)
	
	return center


def make_chair(center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8):
	
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

def make_cup(mc, center, CUP_SIZE, APART_SIZE, SEAT_SIZE):

	## TODO
	## LOCATION argument 추가 필요
	## location : str in ['left', 'right', 'above', 'under']
	
	## make cup
	## under the chair
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
