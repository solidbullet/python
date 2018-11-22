import matplotlib.pyplot as plt  
import pandas as pd
import tushare as ts
import numpy as np
import tushare as ts
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
a = ts.get_industry_classified()
b = a.query('c_name == ["金融行业"]')
#c = a.loc[(a['c_name'] == '综合行业')]
print(b)
#a = ts.get_concept_classified()
#b = a.query('c_name == ["石墨烯"]')
#stocks = ts.get_sz50s()

df = get_ratio('600385')
a = df[-5:-1]
b = df.iloc[-1]
c= a.append(b)
d = df.iloc[-5:-1]
#print(a)