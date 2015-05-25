# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:14:24 2015

@author: Keshav
"""

'''
import numpy as np
from sklearn.cross_validation import train_test_split
a= np.arange(10).reshape((5, 2))
a_train, a_test= train_test_split(a,test_size=0.65, random_state=42)

print a
print ""
print a_train
print ""
print a_test

'''

out = [1,2,3]

print type(out)

test =[]
temp=[]

for iter in out:
    print iter 
    temp.append(iter)
    test.append(temp)
    temp=[]
    
print test