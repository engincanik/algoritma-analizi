
# coding: utf-8

# In[1]:

#matrix_1 mxm
#matrix_2 nxp
#matrix_3 = matrix_1*matrix_2, m*p


# In[2]:

def get_value_from_row_col(r_1,c_1):
    t = 0
    for i in range(len(r_1)):
        t = t+r_1[i]*c_1[i]
    return t
a=[1,2,3,4]
b=[5,6,7,8]
get_value_from_row_col(a,b)


# In[3]:

b=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]] #4x4
a=[[1,2,3,4],[5,6,7,8]] #2x4


# In[15]:

def get_row_from_matrix(a,i):
    return a[i]
def get_col_from_matrix(a,i):
    col = []
    for row in a:
        col.append(row[i])
    #    for indis in range(len(row)):
    #      if(indis==j):
     #           col.apoend(row[indis])
                
    return col
get_row_from_matrix(b,1)


# In[16]:

for item in a:
    print(item)


# In[19]:

def matrix_multiply(m_1,m_2):
    m=len(m_1)
    n=len(m_2[0])
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a = get_row_from_matrix(m_1,i)
            b = get_col_from_matrix(m_2,j)
            c = get_value_from_row_col(a,b)
            r[i].append(c)
    return r
b=[[1,2,3],[5,6,7],[1,2,4],[5,7,8]] #4x4
a=[[1,2,3,4],[5,6,7,8]] #2x4
matrix_multiply(a,b)


# In[13]:

l_1=[1,2,3,4]
l_1[50]=0


# In[ ]:



