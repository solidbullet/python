# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:24:51 2018

@author: jiangyuanqiang
"""

import pandas as pd
from sklearn import svm
from sklearn.linear_model import LogisticRegression
df = pd.read_csv('c:/Users/jiangyuanqiang/bjl.csv')
data = df.iloc[0:60000,0:10].values
target = df.iloc[0:60000,10].values

#clf = svm.LinearSVC(C=1.0, class_weight=None, dual=False, fit_intercept=False,
#     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
#     multi_class='ovr', penalty='l2', random_state=0, tol=1e-05, verbose=0)
#clf.fit(data, target)

clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
clf.fit(data, target)

data_pridict = df.iloc[10000:50000,0:10].values
target_predict = df.iloc[10000:50000,10].values
#print(clf.coef_)
print(clf.score(data_pridict,target_predict))
#print(target_predict)
#print(clf.intercept_)
