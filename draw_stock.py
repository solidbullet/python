import matplotlib.pyplot as plt  
import pandas as pd
import tushare as ts
import numpy as np

def get_ratio(str_code):
    df = pd.DataFrame()
    df = df.append(ts.get_hist_data(str_code))
    if df.empty:
        return 0
    b = df.sort_index(axis = 0,ascending = True)
    r = b.rolling(window = 30,min_periods = 1)
    ma30 = r['close'].aggregate(np.mean)
    std = r['close'].aggregate(np.std)
    #var = r['close'].aggregate(np.var)
    b['ma30'] = ma30
    b['std'] = std
    b['ratio'] = (b['close'] - b['ma30']) /b['std']
    #print(std.tail())
    return b
    
df = get_ratio('002538')
a = df[-120:-1]
b = df.iloc[-1]
df= a.append(b) #最后一行补上，df[-120:-1]读取不出最后一行
print(b)
plt.figure(1)   #创建图表1  

plt.subplot(211) 
plt.ylabel('MA5 M30')
df['ma5'].plot(figsize=(10,6),color='R')
df['ma30'].plot(figsize=(10,6))
df['close'].plot(color='Y')

plt.subplot(212) 
plt.ylabel('RATIO')
df['ratio'].plot(figsize=(10,6))

#plt.show()          #显示所有图表 