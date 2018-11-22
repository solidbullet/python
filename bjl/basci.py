# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 08:42:00 2018

@author: Administrator
"""
import numpy as np
def diff(z, x):
    if z>x:
        r = 1
    elif z<x:
        r = -1
    else:
        r = 0
    return r

def p2(f, s):

    if f > 9:
        f = 0
    if s > 9:
        s = 0
    sum = f+s
    if sum >= 10:
        return sum-10
    else:
        return sum
        
def add(z_point, x_third):
    if z_point < 4 and x_third != 8:
        return True
    elif z_point == 4 and (x_third > 1 and x_third < 8):
        return  True
    elif z_point == 5 and (x_third > 3 and x_third < 8):
        return  True
    elif z_point == 6 and (x_third > 5 and x_third < 8):
        return  True
    else:
        return False
              
c_zhuang = 0
c_xian = 0
c_he = 0
counter = 0
x = np.arange(1,14,1)

for i in range(1000):
    z=x.repeat(32)
    np.random.shuffle(z) 
    while len(z) >= 2:
        if len(z) < 10:
            break
        zhuang = z[0:2]
        xian = z[2:4]
        zhuang_point = p2(zhuang[0],zhuang[1])
        xian_point = p2(xian[0],xian[1])
        if xian_point > 5:#闲不补牌
            if zhuang_point <=5:#闲不补牌的情况下庄补牌
                zhuang_point = p2(zhuang_point,z[4])
                result = diff(zhuang_point,xian_point)
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1        
                z = z[5::]           
            else:#庄闲都不补牌
                result = diff(zhuang_point,xian_point)
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
                z = z[4::]
        else:#闲补牌    
            xian_point = p2(xian_point,z[4])
            is_z_add = add(zhuang_point,z[4])
            if is_z_add:#闲补牌庄补牌
                zhuang_point = p2(zhuang_point,z[5])
                result = diff(zhuang_point,xian_point)
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
                z = z[6::]
            else:#闲补牌庄不补牌
                result = diff(zhuang_point,xian_point)
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1        
                z = z[5::]
    
        counter += 1
#    y = y[4::]
print("庄: ",c_zhuang/counter," 闲: ",c_xian/counter," 和： ",c_he/counter," counter: ",counter)

