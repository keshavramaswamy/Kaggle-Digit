# -*- coding: utf-8 -*-
"""
Created on Fri May 08 16:46:22 2015

@author: Keshav
"""
import pandas as pd
from sklearn.metrics import classification_report
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.lda import LDA
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import cross_val_predict
import numpy as np


traindata =pd.read_csv("train.csv")
testdata = pd.read_csv("test.csv")
print "xyz"
'''
y = traindata['label']
X = traindata.drop('label',axis = 1)
test = testdata

#print len(X)


msk = np.random.rand(len(traindata)) < 0.3
train =  traindata[msk]
test = traindata[~msk]


trainy = train['label']
trainX = train.drop('label',axis = 1)
testy = test['label']
testX = test.drop('label',axis = 1)
'''

from sklearn.cross_validation import train_test_split

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 1000)
'''
train,test= train_test_split(traindata,test_size=0.3, random_state=42)
trainy = train['label']
trainX = train.drop('label',axis = 1)
testy = test['label']
testX = test.drop('label',axis = 1)
'''
traindatay = traindata['label']
traindataX = traindata.drop('label',axis = 1)

forest = forest.fit(traindataX,traindatay)
print forest.n_features_




'''
output = forest.predict(testdata)
print type(output)
output = list(output)
print type(output)

'''

#print forest.score(testX,testy)


'''

test =[]
temp=[]
for iter in output:
    #print iter 
    temp.append(iter)
    test.append(temp)
    temp=[]
    






import csv
csvfile = open('testn1.csv', 'wb')
csvwriter = csv.writer(csvfile)
for item in test:
    csvwriter.writerow(item)
csvfile.close()




'''