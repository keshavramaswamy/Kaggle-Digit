# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:08:11 2015

@author: Keshav
"""

import pandas as pd
from scipy.sparse import csc_matrix
traindata =pd.read_csv("train.csv")
testdata = pd.read_csv("test.csv")
traindatay = traindata['label']
traindataX = traindata.drop('label',axis = 1)
traindataX = csc_matrix(traindataX)
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
#rf = RandomForestClassifier(n_estimators = 100)
et = ExtraTreesClassifier(n_estimators = 1000,n_jobs=-1)
forest = AdaBoostClassifier(et,n_estimators = 1000)
forest = forest.fit(traindataX,traindatay)
output = forest.predict(testdata)
output = list(output)
test =[]
temp=[]
for iter in output:
    #print iter 
    temp.append(iter)
    test.append(temp)
    temp=[]
    
import csv
csvfile = open('testn6.csv', 'wb')
csvwriter = csv.writer(csvfile)
for item in test:
    csvwriter.writerow(item)
csvfile.close()