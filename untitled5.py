# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:15:30 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x, y, z, 103)
mc.setBlock(x, y+1, z, 103)
mc.setBlock(x, y+2, z, 103)
mc.setBlock(x, y+3, z, 103)
mc.setBlock(x, y+4, z, 103)
mc.setBlock(x, y+5, z, 103)
mc.setBlock(x, y+6, z, 103)
mc.setBlock(x, y+7, z, 103)
mc.setBlock(x, y+8, z, 103)
mc.setBlock(x, y+9, z, 103)