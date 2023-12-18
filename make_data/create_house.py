from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()

mc.postToChat('Command Test')

# get position
x, y, z = mc.player.getPos()

# teleport
# mc.player.setPos(x+100, y+100, z+100)

# make whole area empty
mc.setBlocks(x,y,z,100,100,100,block.AIR)

# make stone floor
mc.setBlocks(x,y,z,100,1,100,block.STONE)

# make wood box
mc.setBlocks(x+10,y+2,z+10,20,10,20,block.WOOD)