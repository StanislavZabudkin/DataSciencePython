#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
A = np.array(
    [
        [1, 6],
        [2, 8],
        [3, 11],
        [3, 10],
        [1, 7]
    ]
)
print(A)
print("Размерность A {}".format(A.ndim))
print("Форма A {}".format(A.shape))


# In[13]:


mean_a = A.mean(0)


# In[14]:


mean_a


# In[37]:


C=A-mean_a


# In[38]:


print(C)
print("Размерность C {}".format(C.ndim))
print("Форма C {}".format(C.shape))


# In[52]:


S=0.0
I=0
for D in C:
    print(D)
    S+=D[0]*D[1]
    I+=1
    print(S)


# In[53]:


print(C.shape[0])
S = S/(C.shape[0]-1)
print(f" result of task 3 is {S}")


# In[58]:


task4ResMatr = np.cov(A.transpose())
print(task4ResMatr)


# In[59]:


# we get also 2 !!!


# In[60]:


import pandas as pd


# In[65]:


authors = pd.DataFrame({'author_id':[1,2,3],'author_name':['Pushkin','Tolstoy','Chehov']},
                      columns = ['author_id','author_name'])
books = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3]
                      ,'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники']
                      ,'price':[450, 300, 350, 500, 450, 370, 290]},                     
                      columns = ['author_id','book_title','price'])
print(authors)

print(books)



# In[66]:


authors_price = pd.merge(authors,books, on='author_id',how='inner')
authors_price


# In[68]:


top5 = authors_price.nlargest(5,'price')
top5


# In[ ]:




