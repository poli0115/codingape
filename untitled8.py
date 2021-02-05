# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:44:42 2021

@author: User
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
A1=10
A2=10
A3=20
biock=4
air=0
mc.setBlocks(x,y,z,x+A2,y+A2,z+A1, biock)            
mc.setBlocks(x+1,y+1,z+1,x+A2-1,y+A3-1,z+A1-1,air)