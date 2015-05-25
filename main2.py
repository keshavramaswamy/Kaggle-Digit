# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:50:46 2015

@author: Keshav
"""
import pandas as pd


traindata =pd.read_csv("train.csv")
testdata = pd.read_csv("test.csv")
traindatay = traindata['label']
traindataX = traindata.drop('label',axis = 1)
print "y"

from sklearn import grid_search
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier()
print "x"
parameters = {
    'n_estimators': [1000,2000], 
    'max_features': ['auto', 'sqrt', 'log2']
}
clf = grid_search.GridSearchCV(forest, parameters,cv=10)
clf.fit(traindataX,traindatay)
print "z"
print clf.best_params_ 