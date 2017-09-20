
# coding: utf-8

# In[15]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import os


# In[60]:

os.chdir('C:\python\github\data')
os.getcwd()
#reading data from csv using pandas
df=pd.read_csv('iris.csv')
df.head(2)
#df.info()


# In[61]:

#creating hist only for 1 species at a time versicolor
cd=df[df.species=='versicolor']
df=cd.petal_length


# In[66]:

#use numpy square root method to define bins
new_bin=int(np.sqrt(len(df)))


# In[65]:

_=plt.hist(df,bins=new_bin)
_=plt.xlabel('petal_length(cm)')
_=plt.ylabel('count')
plt.show()


# In[ ]:



