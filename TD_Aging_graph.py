# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:15:37 2019

@author: Rahul Varshney
"""
import pandas as pd
from numpy import *

dataset = pd.read_csv('aging_mean.csv')
dfsize=dataset['index'].size
x=[]
for i in range(dfsize):
 x.append(i)
#x = dataset.iloc[:, :-1].values
#x=dataset['index'].values
#x=dataset['index'].
y=dataset['mean'].values

#y = dataset.iloc[:, 1].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_x=LabelEncoder()
x=labelencoder_x.fit_transform(x)



#x= array([0,1,2,3,4,5])
#y=array([0,0.8,0.9,0.1,-0.8,-1])
from scipy.interpolate import *
p1=polyfit (x,y,1)
from matplotlib.pyplot import *
#plot(x,y,'o')
plot(x,y,y)
plot(x,polyval(p1,x),'r-')
plt.savefig('ageplot.png')