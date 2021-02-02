# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:36:59 2021

@author: User
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
a=0
flower=38
while True:
    x,y,z=mc.player.getTilePos()
    color=random.randrange(0,9)
    mc.setBlock(x,y,z,flower,color)
    time.sleep(0.2)
    a=a+1
    