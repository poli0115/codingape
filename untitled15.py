# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:07:27 2021

@author: User
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"我愛",  "Minecraft,","也愛python")

