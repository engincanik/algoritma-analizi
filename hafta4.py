#!/usr/bin/env python
# coding: utf-8

# In[11]:


#matrix_1 mxn
#matrix_2 nxp
#matrix_3 = matrix_1 * matrix_2  , mxp

import numpy as np
def get_value_from_row_col(r_1,c_1):     #O(n)
    t = 0
    for i in range(len(r_1)):
        t = t + r_1[i] * c_1[i]
    return t

a=[1,2,3,4]
b=[5,6,7,8]
get_value_from_row_col(a,b)


# In[12]:




b=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]] #4x4
a=[[1,2,3,4],[5,6,7,8]]  #2x4


# In[13]:




def get_row_from_matrix(matrix,i):
    return matrix[i]

def get_col_from_matrix(matrix,j):
    col=[]
    for row in range(len(matrix)):
        col.append(matrix[row][j])
    return col

get_row_from_matrix(a,1)
get_col_from_matrix(b,1)


# In[9]:


def rec_fb(n, result): #recursive fibonacci kodunun karmaşıklığının daha sade hali
    if n<2:
        return n
    elif(result[n] != 0):
        return result[n]
    else:
        result[n] = rec_fb(n-1, result) + rec_fb(n-2, result)
        return result[n]
    
for i in range(13,25):
    print(rec_fb(i,[0]*(i+1)), end=" ")


# In[14]:


def matrix_multiply(m_1,m_2): #karmaşıklık O(mnp)    , matris kareyse O(n^3)
    m = len(m_1) #1. matrisin satır sayısı
    n = len(m_2[0]) #2. matrisin sütun sayısı
    r=[]
    
    if(len(m_1[0]) != len(m_2)): return "Boyutlar uyumsuz, matrisler çarpılamaz"
    else:
        for i in range(m):
            r.append([])
            for j in range(n):
                a = get_row_from_matrix(m_1,i)
                b = get_col_from_matrix(m_2,j)
                c = get_value_from_row_col(a,b)
                r[i].append(c)
        return r
    
matrix_multiply(a,b)


# In[15]:



def matrix_multiply_v2(m_1,m_2):
    m = len(m_1) #1. matrisin satır sayısı
    n = len(m_2[0]) #2. matrisin sütun sayısı
    r = np.zeros(shape=(m,n))
    
    if(len(m_1[0]) != len(m_2)): return "Boyutlar uyumsuz, matrisler çarpılamaz"
    else:
        for i in range(m):
            for j in range(n):
                a = get_row_from_matrix(m_1,i)
                b = get_col_from_matrix(m_2,j)
                c = get_value_from_row_col(a,b)
                r[i][j] = c
        return r

matrix_multiply_v2(a,b)


# In[ ]:




