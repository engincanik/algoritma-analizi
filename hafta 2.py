#!/usr/bin/env python
# coding: utf-8

# In[10]:


import ctypes


# In[60]:


class DynamicArray:
    
    def __init__(self):
        self._n=0# count actual elements
        self._capacity = 1# default array capacity
        self._A=self.makearray(self._capacity)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        
        if not 0<= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    def append(self,obj):
        
        if self._n==self._capacity:# not enough room
            self.resize(2 * self._capacity)# so double capacity
        self._A[self._n] = obj
        self._n+=1
        print("OKA")
            
    def resize(self,c):
        # nonpublic utitity
        print("worst-case list full")
        print("n*2lik yerden tasima yapilacak")
        B=self.makearray(c)# new (bigger) array
        for k in range(self._n):# for each existing value
            B[k] =self._A[k]
        self._A=B# use the bigger array
        self._capacity = c
    def makearray(self,c):
        # nonpublic utitity
        
        return(c * ctypes.py_object)()
    
    def getLength(self):
        return self.__len__()


# In[61]:


c = DynamicArray()
for i in range(10):
    c.append(str(i))
#print("length: ", c.getLength())
c.append("qasdasd")
c.append("qasasd")
c.append("qassd")
c.append("qasda")
print("length: ", c.__len__())

