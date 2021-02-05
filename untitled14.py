# -*- codin')g: utf-8 -*-
"""
Created on Tue Feb  2 15:19:51 2021

@author: User
"""

from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
try:
    blockType=int(input("輸入你要的方塊 ID:"))
    mc.setBlock(x,y,z, blockType ) 
except:
    print("只能輸陸數字!!")