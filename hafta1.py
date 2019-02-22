
# coding: utf-8

# In[25]:

global s
s = 0
def power(x,n):
    global s
    s = s + 1
    if(n==0):
        return 1
    if(n==1):
        return x
    if(n%2==0):
        return power(x*x,n/2)
    else:
        return power(x*x,n/2)*x


# In[26]:

print(power(2,2))
print(s)


# In[ ]:



