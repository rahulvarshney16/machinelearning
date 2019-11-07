# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:01:46 2019

@author: Rahul Varshney
"""

import pandas as pd

train =pd.read_csv('prod.csv')
train.groupby('Case Owner: Full Name')[['Case Age For Reports']].mean()

train.groupby(['Case Owner: Full Name','Product: Product Name'])['Case Age For Reports'].aggregate('mean')

train.pivot_table('Case Age For Reports', index='Case Owner: Full Name')

df=pd.DataFrame(train.pivot_table('Case Age For Reports', index='Case Owner: Full Name'))
df=df.round(0)

##################################################################################
####################INPUT FOR THE CURRENT MONTH REQUIRED BELOW####################
##################################################################################
df.rename(columns={'Case Age For Reports':'Octt19'},inplace=True)
df.to_csv('aging_current_month.csv')


df2=pd.read_csv('old_aging.csv')
df3=pd.merge(df2, df, on='Case Owner: Full Name', how='outer')
df3=df3[df3['Case Owner: Full Name'].map(lambda x: str(x)!="Raju Kaul")]
df3=df3[df3['Case Owner: Full Name'].map(lambda x: str(x)!="Nidhi Leekha")]
df3=df3[df3['Case Owner: Full Name'].map(lambda x: str(x)!="Abhinav Aggarwal")]
df3=df3[df3['Case Owner: Full Name'].map(lambda x: str(x)!="Sandeep Kumar")]
df3=df3[df3['Case Owner: Full Name'].map(lambda x: str(x)!="Saroj Kumar Jha")]
#df3.drop(['Nidhi Leekha', 'Raju Kaul'])
df3.to_csv('Old_Current_Aging.csv')

df4=df3.describe()
#df = df.drop(df.columns[[0]], axis=1)
#df3.mean(axis=0)
df4=df4.transpose()
df4 = df4.reset_index()
##df3 = df3.set_index(df3.iloc[:, 0])
#list(df3.columns.values) 
#df3=df3.head()
#df3
df4.to_csv('aging_mean.csv')

#df4=df3.mean()
#df4=df4.round(0)
#df4=df4.columns=["Month","Age"]

import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('aging_mean.csv')
data = csv[['mean','index']]
x = data['index']
y = data['mean']
plt.scatter(x,y)


#z = np.polyfit(x, y, 1)
z = np.polynomial.polynomial.polyfit(x, y, 1)
#z=np.polyfit(x,y,1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

#print "y=%.6fx+(%.6f)"%(z[0],z[1])
plt.show()







