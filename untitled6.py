# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:33:57 2021

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x, y, z, 103)
mc.setBlock(x+1, y, z, 103)
mc.setBlock(x+2, y, z+1, 103)
mc.setBlock(x+2, y, z+1, 103)
mc.setBlock(x, y, z+2, 103)
mc.setBlock(x+1, y, z, 103)
mc.setBlock(x+2, y, z, 103)
mc.setBlock(x+2, y, z+2, 103)
mc.setBlock(x, y, z+1, 103)





























