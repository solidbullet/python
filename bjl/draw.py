# -*- coding: utf-8 -*-
#剩余单张牌的数量来模拟概率
import matplotlib.pyplot as plt
import numpy as np
c_zhuang = 0#庄赢的次数
ya_zhuang_sum = 0
ya_zhuang_win_sum = 0
c_xian = 0#闲赢的次数
c_he = 0#和的次数


#xian_10 = 0
#he_10 = 0

counter = 0
yazhuang_counter = 0
c_z10 = []
c_win = 0
def diff(z, x):#庄赢1，闲赢-1，和是0
    if z>x:
        r = 1
    elif z<x:
        r = -1
    else:
        r = 0
    return r

def p2(f, s):#返回前两张牌加起来的点数

    if f > 9:
        f = 0
    if s > 9:
        s = 0
    sum = f+s
    if sum >= 10:
        return sum-10
    else:
        return sum
        
def add(z_point, x_third):#庄是否补牌
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

def play(z):#玩一局牌
    global c_zhuang 
    global c_xian
    global c_he
    global counter
    global yazhuang_counter
    global c_win
    global ya_zhuang_sum
    global ya_zhuang_win_sum
    rand_play_time = 10
    ya_zhuang_win_within_done = 0
    ya_zhuang_within_done_sum = 0
    ya_zhuang_win_within_10 = 0
    kaiguan = 0
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
                    #print(z)
                z = z[5::]  #通过上面的操作把运算过的牌去掉，只保留剩下的牌

            else:#庄闲都不补牌
                result = diff(zhuang_point,xian_point)
#                if z.tolist().count(left_num) == left_counter:
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
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
                    #print(z)
                z = z[6::]

            else:#闲补牌庄不补牌
                result = diff(zhuang_point,xian_point)
                if result == 1:
                    c_zhuang += 1
                elif result == -1:
                    c_xian += 1
                elif result == 0:
                    c_he += 1
                    #print(z)
                z = z[5::]
        if kaiguan == 0:
            rand_play_time = rand_play_time - 1#计数器，每玩1局减1
        else:
            rand_paly_time = 10
        if result == 1 and kaiguan == 0:#如果庄赢+1
            ya_zhuang_win_within_10 += 1 #统计10局内庄赢的次数，10次内小于3次就开始押注
        #print("rand_play_time: ",rand_play_time," ya_zhuang_win_within_10 ",ya_zhuang_win_within_10)
        if rand_play_time == 0:
            if ya_zhuang_win_within_10 <= 3:
                kaiguan = 1
                ya_zhuang_sum += 1
                ya_zhuang_within_done_sum += 1
                if result == 1:
                    ya_zhuang_win_sum += 1
                    ya_zhuang_win_within_done += 1
            else:#如果不满足10次内仅仅中3次庄的话，那就归零重新来
                rand_play_time = 10
                kaiguan = 0
                ya_zhuang_win_within_10 = 0
                ya_zhuang_win_within_done=0
                ya_zhuang_within_done_sum=0
        if ya_zhuang_within_done_sum >9 and ya_zhuang_win_within_done/ya_zhuang_within_done_sum >= 0.7:
        #if ya_zhuang_within_done_sum ==20:
            rand_play_time = 10
            kaiguan = 0
            ya_zhuang_win_within_10 = 0
            ya_zhuang_win_within_done=0
            ya_zhuang_within_done_sum=0
   
        counter += 1    
#        if counter%10 == 0:
#            if c_zhuang <= 3:
#            c_z10.append(c_zhuang)
#            c_zhuang = 0
#            c_xian = 0
#            c_he = 0
    
x = np.arange(1,14,1)

for i in range(10000):
    z=x.repeat(32)
    np.random.shuffle(z)#生成牌局
    play(z)
print(ya_zhuang_win_sum,ya_zhuang_sum,ya_zhuang_win_sum/ya_zhuang_sum)
#print(c_z10)

#plt.figure(1,figsize=(12,5))   #创建图表1  
#plt.plot(c_z10)
#plt.show()


#开仓逻辑：如果10次里面押庄中标次数小于3次，那么就一直押庄；出场：1、有仓位2、10次里面押庄中的次数超过6次，或者收益超过20%
#print("庄: ",round(c_zhuang,4)," 闲: ",round(c_xian,4)," 和： ",round(c_he,4)," 压庄局数: ",yazhuang_counter," 总局数: ",counter)

#if z.tolist().count(left_num) == left_counter: