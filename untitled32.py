# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:30:36 2021

@author: User
"""

from mcpi.minecraft import Minecraft
from random import randrange
mc=Minecraft.create()
r= randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWeithData(hit.pos)
        data=block.data
        
        if data==r:
            mc.postToChat("恭喜你找到我")
            mc.setBlock(hit.pos, 57)
            break
        elif data < r:
            mc.postToChat("找錯摟!找找比我更大的顏色")
        elif data < r:
            mc.postToChat("找錯摟!找找比我更小的顏色")