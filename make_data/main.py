from mcpi.minecraft import Minecraft
from javascript import require, On
import mcpi.block as block
from mcpi.connection import Connection
import argparse
import time


# parser = argparse.ArgumentParser()
# parser.add_argument("--number_of_samples", type=int, help="how many samples to make")
# parser.add_argument("--field_size", type=int, help="how many samples to make")
# parser.add_argument("--apart_size", type=int, help="how many samples to make")
# parser.add_argument("--leg_size", type=int, help="how many samples to make")
# parser.add_argument("--seat_size", type=int, help="how many samples to make")
# parser.add_argument("--cup_size", type=int, help="how many samples to make")

# args = parser.parse_args()

def clear_and_make_space(mc, center, size = 50):
        
    ## clear area
    mc.setBlocks(center.x - size, 
                 center.y, 
                 center.z - size, 
                 center.x + size, 
                 center.y + size, 
                 center.z + size,
                 block.AIR)
    
    ## make floor
    mc.setBlocks(center.x - size, 
                 center.y - 1, 
                 center.z - size, 
                 center.x + size, 
                 center.y - 1, 
                 center.z + size,
                 block.STONE)
    
    # make wall
    mc.setBlocks(center.x - size, 
                 center.y, 
                 center.z - size, 
                 center.x - size, 
                 center.y + size, 
                 center.z + size,
                 block.STONE)
    mc.setBlocks(center.x - size, 
                 center.y, 
                 center.z - size, 
                 center.x + size, 
                 center.y + size, 
                 center.z - size,
                 block.STONE)
    mc.setBlocks(center.x + size, 
                 center.y, 
                 center.z - size, 
                 center.x + size, 
                 center.y + size, 
                 center.z + size,
                 block.STONE)
    mc.setBlocks(center.x - size, 
                 center.y, 
                 center.z + size, 
                 center.x + size, 
                 center.y + size, 
                 center.z + size,
                 block.STONE)
    
def make_chair(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8):

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
    
def make_cup_chair_beneath(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4):
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y+1, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y+1, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) , 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) - 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)
    
def make_cup_chair_above(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4):
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + LEG_SIZE + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + LEG_SIZE + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + LEG_SIZE + 2 + 1, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + LEG_SIZE + 2 + 1, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3) , 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3) - 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)


def make_cup_chair_right(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_RIGHT = 5):
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y ,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y ,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + 1,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + 1,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) - 2, 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)
    

def make_cup_chair_left(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_LEFT = 5):  
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y ,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y ,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + 1,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + 1,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block.GOLD_ORE)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block.GOLD_ORE)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) - 2, 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block.GOLD_ORE)


if __name__ == "__main__":

    ## create minecraft instance
    address, port = 'localhost', 4711 #### default setting
    conn = Connection(address, port)
    mc = Minecraft(conn).create()
    center = mc.player.getPos()

    clear_and_make_space(mc, center, size = 50)
    make_chair(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8)

    time.sleep(15)

    for i in range(5):
        if i % 2 == 1 :
            make_cup_chair_left(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_LEFT = 5)
        
        else:
            make_cup_chair_right(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_RIGHT = 5)












