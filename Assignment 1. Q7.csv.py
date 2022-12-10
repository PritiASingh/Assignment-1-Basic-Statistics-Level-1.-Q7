#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


cars=pd.read_csv("Q7.csv")


# In[4]:


cars


# In[5]:


cars.mean()


# In[6]:


cars.median()


# In[7]:


cars.Points.mode() 


# In[8]:


cars.Score.mode()


# In[9]:


cars.Weigh.mode()


# In[10]:


cars.var()


# In[11]:


cars.std()


# In[12]:


cars.describe()


# In[13]:


Points_Range=cars.Points.max()-cars.Points.min()
Points_Range


# In[14]:


Score_Range=cars.Score.max()-cars.Score.min()
Score_Range


# In[15]:


Weigh_Range=cars.Weigh.max()-cars.Weigh.min()
Weigh_Range


# In[16]:


f,ax=plt.subplots(figsize=(15,5))
plt.subplot(1,3,1)
plt.boxplot(cars.Points)
plt.title('Points')
plt.subplot(1,3,2)
plt.boxplot(cars.Score)
plt.title('Score')
plt.subplot(1,3,3)
plt.boxplot(cars.Weigh)
plt.title('Weigh')
plt.show()


# In[ ]:




