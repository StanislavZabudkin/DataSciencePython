#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[6]:


a = [2,5,7,9,11]


# In[7]:


b = pd.Series(a)


# In[8]:


b


# In[9]:


b = pd.Series(a,index= [0,1,2,3,4])


# In[10]:


b


# In[11]:


b = pd.Series(a,index=['a','b','c','d','e'])


# In[12]:


b


# In[14]:


from datetime import date


# In[16]:


ind = [date(y,m,d) for y,m,d in [(2018,1,15),(2018,1,17),(2018,1,19),(2018,1,21),(2018,1,23)]]


# In[19]:


b = pd.Series(a,index = ind)


# In[20]:


b


# In[21]:


b.index


# In[22]:


b.index[0].year


# In[23]:


b.index[0].day


# In[24]:


b.index = pd.to_datetime(b.index, format='%Y-%m-%d')


# In[25]:


b.index


# In[26]:


b.index.year


# In[27]:


b.index.month


# In[28]:


b.index.day


# In[30]:


b = pd.Series(a,index = [0,1,0,2,1])


# In[31]:


b


# In[32]:


b.index = [10,11,12,13,14]
b


# In[33]:


b = pd.Series(a,dtype = np.float64)


# In[34]:


b


# In[35]:


b = pd.Series(a)
b = b.astype(np.float64)
b


# In[36]:


d = {'1st':'a','2st':'b','3st':'c','4st':'d','5st':'e'}
b = pd.Series(d)
b


# In[37]:


b = pd.Series([5,7,2,3,4,5,6,7,8,9,90])
b.index


# In[38]:


b.values


# In[39]:


b[0]


# In[40]:


b[3]


# In[42]:


b[[1,2,5]]


# In[43]:


b.head()


# In[44]:


b.head(3)


# In[45]:


b.tail()


# In[46]:


b.tail(3)


# In[47]:


b


# In[48]:


b[b>5]


# In[49]:


b[(b==7)|(b%3 ==0)]


# In[50]:


b


# In[51]:


b[5] = -5


# In[52]:


b


# In[53]:


b[b<5]=0


# In[54]:


b


# In[55]:


b[[0,1,2]] = -999


# In[56]:


b


# In[59]:


b = b.append(pd.Series({1:1, 3:3, 101:101}))
b


# In[60]:


b = b.drop([0,1,2])


# In[61]:


b


# In[62]:


b.to_pickle('b.pkl')


# In[63]:


b2 = pd.read_pickle('b.pkl')


# In[64]:


b2


# In[ ]:




