# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:59:42 2021

@author: User
"""
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
color=random.randrange(0,16)
mc.setBlocks(x-50,y-1,z-50,x-1,y-1,z+50,138,color)              