# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:55:06 2021

@author: User
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
number=1
x,y,z=mc.player.getTilePos()
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    number=number*2
    mc.postToChat("這次生成了"+str(number)+"隻蠹魚")
    time.sleep(1)