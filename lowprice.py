import tushare as ts
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)

col_n = ['code','name','trade']

all_stocks = ts.get_today_all()  
a = pd.DataFrame(all_stocks,columns = col_n) 
a = a[(a.trade > 2) &(a.trade < 4)]
a.to_excel('c:/day/1.xlsx')
print(a.sort_values(by = 'trade'))
#stocks = ts.get_hs300s()
#stocks = ts.get_sz50s()
#a = ts.get_industry_classified()
#stocks = a.query('c_name == ["生物制药"]')
a = ts.get_concept_classified()
stocks = a.query('c_name == ["生物疫苗"]')
#ratio = np.arange(300)
#print(sz50)

#dfratio = pd.DataFrame(index = np.arange(len(stocks)),columns=['price','code','name'])
#
#for i in range(len(stocks)):
#    code = stocks['code'].iloc[i]
#    if(ts.get_hist_data(str(code)) is None):
#        continue
#    #ts.get_hist_data(code).iloc[0]['close'])
#    dfratio['price'][i] = ts.get_hist_data(code).iloc[0]['close']
#    dfratio['code'][i] = code
#    dfratio['name'][i] = stocks['name'].iloc[i]
##    print(ts.get_hist_data(code) is None,' I: ',i)
#print(dfratio.sort_values(by = 'price'))

    

