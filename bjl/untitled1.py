# -*- coding: utf-8 -*-
#剩余单张牌的数量来模拟概率
import numpy as np
import csv
with open('bjl.csv', 'w', newline='') as csvfile:
    fieldnames = ['zero', 'one','two','three','four','five','six','seven','eight','nine','result']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
dict = {'zero': 0, 'one': 0, 'two': 0,'three':0,'four':0, 'five': 0, 'six': 0,'seven':0,'eight':0,'nine':0,'result':1}
c_zhuang = 0
c_xian = 0
c_he = 0
counter = 0
yazhuang_counter = 0
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

def play(z):
    global c_zhuang 
    global c_xian
    global c_he
    global counter
    global yazhuang_counter
    left_num =8
    left_counter = 0
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
#                if z.tolist().count(left_num) == left_counter:
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
                yazhuang_counter += 1
                    #print(z)
                z = z[5::]

            else:#庄闲都不补牌
                result = diff(zhuang_point,xian_point)
#                if z.tolist().count(left_num) == left_counter:
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
                yazhuang_counter += 1
                    #print(z)
                z = z[4::]

        else:#闲补牌    
            xian_point = p2(xian_point,z[4])
            is_z_add = add(zhuang_point,z[4])
            if is_z_add:#闲补牌庄补牌
                zhuang_point = p2(zhuang_point,z[5])
                result = diff(zhuang_point,xian_point)
#                if z.tolist().count(left_num) == left_counter:
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
                yazhuang_counter += 1
                    #print(z)
                z = z[6::]

            else:#闲补牌庄不补牌
                result = diff(zhuang_point,xian_point)
#                if z.tolist().count(left_num) == left_counter:
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
                yazhuang_counter += 1 
                    #print(z)
                z = z[5::]
        
        counter += 1
#        dict = {'zero': 0, 'one': 0, 'two': 0,'three':0,'four':0, 'five': 0, 'six': 0,'seven':0,'eight':0,'nine':0,'result':1}
        dict['zero'] = z.tolist().count(10)+z.tolist().count(11)+z.tolist().count(12)+z.tolist().count(13)
        dict['one'] = z.tolist().count(1)
        dict['two'] = z.tolist().count(2)
        dict['three'] = z.tolist().count(3)
        dict['four'] = z.tolist().count(4)
        dict['five'] = z.tolist().count(5)
        dict['six'] = z.tolist().count(6)
        dict['seven'] = z.tolist().count(7)
        dict['eight'] = z.tolist().count(8)
        dict['nine'] = z.tolist().count(9)
        dict['result'] = result
        with open('bjl.csv', 'a', newline='') as csvfile:
            fieldnames = ['zero', 'one','two','three','four','five','six','seven','eight','nine','result']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict)
              

x = np.arange(1,14,1)

for i in range(1000):
    z=x.repeat(32)
    np.random.shuffle(z)
    play(z)
    
print("庄: ",round(c_zhuang,4)," 闲: ",round(c_xian,4)," 和： ",round(c_he,4)," 压庄局数: ",yazhuang_counter," 总局数: ",counter)
