from mcpi.minecraft import Minecraft
from javascript import require, On
import mcpi.block as block
from mcpi.connection import Connection
import argparse
import time
from PIL import ImageGrab
import numpy as np
import cv2
import yaml
import random
from datetime import datetime
import pyautogui


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
    
def make_chair(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, block_id = 1):

    ## make legs
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
                 center.y, 
                 center.z - APART_SIZE - SEAT_SIZE, 
                 center.x - APART_SIZE - SEAT_SIZE, 
                 center.y + LEG_SIZE, 
                 center.z - APART_SIZE - SEAT_SIZE,
                 block_id)

    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
                 center.y, 
                 center.z - APART_SIZE, 
                 center.x - APART_SIZE - SEAT_SIZE, 
                 center.y + LEG_SIZE, 
                 center.z - APART_SIZE, 
                 block_id)

    mc.setBlocks(center.x - APART_SIZE, 
                 center.y, 
                 center.z - APART_SIZE - SEAT_SIZE, 
                 center.x - APART_SIZE, 
                 center.y + LEG_SIZE, 
                 center.z - APART_SIZE - SEAT_SIZE, 
                 block_id)

    mc.setBlocks(center.x - APART_SIZE, 
                 center.y, 
                 center.z - APART_SIZE, 
                 center.x - APART_SIZE, 
                 center.y + LEG_SIZE, 
                 center.z - APART_SIZE, 
                 block_id)
    
    # make seat
    mc.setBlocks(center.x - APART_SIZE, 
                 center.y + LEG_SIZE + 1, 
                 center.z - APART_SIZE, 
                 center.x - APART_SIZE - SEAT_SIZE, 
                 center.y + LEG_SIZE + 1, 
                 center.z - APART_SIZE - SEAT_SIZE, 
                 block_id)
    
    # make back
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
                center.y + LEG_SIZE   + 1, 
                center.z - APART_SIZE - SEAT_SIZE, 
                center.x - APART_SIZE - SEAT_SIZE, 
                center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
                center.z - APART_SIZE - SEAT_SIZE, 
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
                center.y + LEG_SIZE   + 1, 
                center.z - APART_SIZE, 
                center.x - APART_SIZE - SEAT_SIZE, 
                center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
                center.z - APART_SIZE, 
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE, 
                center.y + LEG_SIZE   + 1 + LEG_SIZE//2, 
                center.z - APART_SIZE , 
                center.x - APART_SIZE - SEAT_SIZE, 
                center.y + LEG_SIZE   + 1 + LEG_SIZE, 
                center.z - APART_SIZE - SEAT_SIZE, 
                block_id) 
    
def make_cup_chair_beneath(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, block_id = 1):
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y+1, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y+1, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) , 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) - 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)
    
def make_cup_chair_above(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, block_id = 1):
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + LEG_SIZE + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + LEG_SIZE + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + LEG_SIZE + 2 + 1, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + LEG_SIZE + 2 + 1, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3) , 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3) - 2, 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + LEG_SIZE + 2 + 2 + (CUP_SIZE - 3), 
                center.z - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)


def make_cup_chair_right(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_RIGHT = 5, block_id = 1):
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y ,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y ,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + 1,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + 1,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2,
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) - 2, 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z - HOW_FAR_TO_RIGHT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)
    

def make_cup_chair_left(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_LEFT = 5, block_id = 1):  
    # Cup floor?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y ,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y ,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.y + 1,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2+1, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1, 
                center.y + 1,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2-1,
                block_id)
    # Cup wall?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2,
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2, 
                center.x - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3),
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2+CUP_SIZE//2,
                block_id)
    # Cup handle?
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 1, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)
    mc.setBlocks(center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3) - 2, 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2, 
                center.x - APART_SIZE - SEAT_SIZE//2, 
                center.y + 2 + (CUP_SIZE - 3), 
                center.z + HOW_FAR_TO_LEFT * 2 - APART_SIZE - SEAT_SIZE//2-CUP_SIZE//2 - 2,
                block_id)


if __name__ == "__main__":

    ## create minecraft instance
    
    address, port = 'localhost', 4711 #### default setting
    conn = Connection(address, port)
    mc = Minecraft(conn).create()
    center = mc.player.getPos()
    with open('block_config.yaml') as f:
        block_info = yaml.load(f, Loader=yaml.FullLoader)
    
    # wait to maximize the size of Chrome to full screen
    mc.postToChat('Minecraft server activated')

    clear_and_make_space(mc, center, size = 50)
    make_chair(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, block_id = 2)

    mc.postToChat('Please Check the direction for the chair')
    time.sleep(15)

    block_list = list(block_info.keys())

    for i in range(800):

        # choice block
        chair_block = random.choice(block_list)
        cup_block   = random.choice(block_list)
        
        while chair_block == cup_block :
            cup_block   = random.choice(block_list)
        
        if i == 0:
            mc.postToChat('block size choice done')
        
        chair_block_id = block_info[chair_block]
        cup_block_id   = block_info[cup_block]

        # choice position of the cup
        positions = ['left', 'right', 'above', 'beneath']

        # clear space
        clear_and_make_space(mc, center, size = 50)
        # make chair
        make_chair(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, block_id = chair_block_id)
        
        # make cup
        where_to = random.choice(positions)

        if where_to == 'left' :
            make_cup_chair_left(mc,  center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_LEFT = 5,  block_id = cup_block_id)
        if where_to == 'right' :
            make_cup_chair_right(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, HOW_FAR_TO_RIGHT = 5, block_id = cup_block_id)
        if where_to == 'above' :
            make_cup_chair_above(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, block_id = cup_block_id)
        if where_to == 'beneath' :
            make_cup_chair_beneath(mc, center, APART_SIZE = 3, LEG_SIZE = 8, SEAT_SIZE = 8, CUP_SIZE = 4, block_id = cup_block_id)

        # screen shot
        # img = ImageGrab.grab(bbox=(100,10,400,780)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
        time.sleep(2)
        # img = ImageGrab.grab() #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
        # img_np = np.array(img) #this is the array obtained from conversion
        # frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        myScreenshot = pyautogui.screenshot()

        # local path to save images
        now_ = datetime.now()
        now_string = now_.strftime('%Y-%m-%d-%H-%M-%S')
        file_name = chair_block + '_' + cup_block + '_' + where_to + '_' + now_string
        image_path = 'C:/Users/jhoonpark/Desktop/minecraft_sample_images/' + file_name + '.png'
        print('image_path : ', image_path)

        myScreenshot.save(image_path)
        
        # if i % 10 == 0:
        #     cv2.imshow("test", frame)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
        
        time.sleep(1)












