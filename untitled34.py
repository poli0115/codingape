# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:09:22 2021

@author: User
"""

from random import randrange
from time import time
def linearSearch():
    sTime=time()
    low=0
    top=10000000
    while iow<=top:
        mid=(low+top)//2
        if mid < number:
            low=mid+1
        elif mid>number:
            top=mid-1
        elif:
            print("找到答案了!是"+str(i))
            print("二元搜尋法,花了"+str(time()-sTime)+"秒")
            break
number=randrange(1,10000001)
linearSearch()       
        
        