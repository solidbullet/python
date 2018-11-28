# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:41:11 2018

@author: jiangyuanqiang
"""

import tushare as ts
import pandas as pd
import numpy as np
col_n = ['name','pe','pb','bvps','esp']


df = ts.get_stock_basics()
a = pd.DataFrame(df,columns = col_n)
a = a[(a.pb > 0) &(a.esp > 0.5)]
not_ST = ~a.name.str.contains('ST')
a = a[not_ST]
not_cyb = ~a.index.str.startswith('300')
a= a[not_cyb]

#b = a.iloc[0:100,12:15]
a.to_excel('c:/day/2.xlsx')
#print(a.sort_values(by = 'pb',ascending=True))
#print(a.sort_values(by = 'trade'))  ~df.col3.str.contains('u|z')