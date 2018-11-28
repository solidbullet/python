import matplotlib.pyplot as plt  
import pandas as pd
import tushare as ts
import numpy as np

#a=ts.get_hist_data('600848', ktype='5') #获取5分钟k线数据
#print(a.head())
a = pd.read_csv('d:/a.csv',sep='\s+')
print(a.head())
print(a.iloc[1])
#plt.show()          #显示所有图表 