from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()

mc.postToChat('Make Chair')

# get position
pos = mc.player.getPos()
direction = mc.player.getDirection()

## 아무것도 안 한 상태라면 
## direction.x = 0.32, direction.y = 0.11, direction.z = 0.93

# make empty space
BLOCKDISTANCE = 5
x_ = round(pos.x + (direction.x * BLOCKDISTANCE))
y_ = round(pos.y + (direction.y * BLOCKDISTANCE) + 1)
z_ = round(pos.z + (direction.z * BLOCKDISTANCE))

mc.setBlocks(pos.x, pos.y, pos.z, x_, y_, z_, block.AIR)

# make stone floor
mc.setBlocks(pos.x, pos.y, pos.z, x_, pos.y+1, z_, block.STONE)

# make wall
WALL_SIZE = 30
mc.setBlocks(pos.x, pos.y, z_, x_, pos.y+WALL_SIZE, z_, block.STONE)
mc.setBlocks(x_, pos.y, pos.z, x_, pos.y+WALL_SIZE, z_, block.STONE)

# move to center
center_x = pos.x + (x_ - pos.x) // 2
center_z = pos.z + (z_ - pos.z) // 2

mc.player.setPos(center_x, pos.y+2, center_z)

## make chair
center = mc.player.getPos()

APART_SIZE = 10
LEG_SIZE = 5
SEAT_SIZE = 5

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

## make cup
CUPSIZE = 3
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

