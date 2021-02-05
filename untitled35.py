# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:38:40 2021

@author: User
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()
myID=mc.getPlayerEntityId("Poli_Tu")
mc.postToTitle(myID, "Hello")