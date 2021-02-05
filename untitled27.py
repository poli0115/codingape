# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:17:35 2021

@author: User
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
list1=[]
list2=[]
list3=[]
for i in range(1,4):
    list1.append(1*i)
for i in range(1,4):
    list2.append(2*i)
for i in range(1,4):
    list3.append(3*i)
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,2,str(list1),str(list2),str(list3))
    