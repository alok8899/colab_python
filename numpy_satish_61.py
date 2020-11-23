#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hai")


# In[5]:





# In[29]:


sdarray=np.array([[11,45,55]])


# In[30]:


print(sdarray)


# In[33]:


import numpy as np
mdarray=np.array([[12,44,555],[22,452,42]])
print(mdarray)
print("the dimention of array is ",mdarray.ndim)
print("the size of array is ",mdarray.itemsize,"byte")
print("the datatype of array is ",mdarray.dtype)
print("the size of array is ",mdarray.size)
print("the shape of array is ",mdarray.shape)
reshapemdarray=mdarray.reshape(3,2)
print(reshapemdarray)
print("the dimention of array is ",reshapemdarray.ndim)
print("the size of array is ",reshapemdarray.itemsize,"byte")
print("the datatype of array is ",reshapemdarray.dtype)
print("the size of array is ",reshapemdarray.size)
print("the shape of array is ",reshapemdarray.shape)


# In[7]:


import numpy as np
mdarray=np.array([[12,44,555,22],[22,452,42,66],[1,52,63,88],[92,42,36,44],[1,2,3,4]])
print(mdarray)
print("the slicing element (0,2) is:- ",mdarray[0,2])
print("the 2nd column data (0:,2) is:-\n ",mdarray[0:,2]) #(row,column)
print("the 3rd row data (2,0:) is:-\n ",mdarray[2,0:]) #(row,column)
print("the 3rd row data (0:2,1) is:-\n ",mdarray[0:2,1])
print("the 3rd row data (1:4,1) is:-\n ",mdarray[1:4,1]) #1:4 means 1 to (4-1)
print("the 3rd row data (1:2,1) is:-\n ",mdarray[1:2,1])


# In[10]:



#! python3

import os
os.system("cls")

import numpy as np

sdarray = np.array([[10,17,25]])
mdarray = np.array([[10,17,25],[1,5,7]])
mdarray2 = np.array([[10,17,25],[1,5,7]],dtype=float)

print("printing the original element from the array")
print(sdarray)
print(mdarray2)
print(mdarray)
print("the array dimention is",mdarray.ndim)
print("the array size is",mdarray.size)
print("the array shape is",mdarray.shape)
print("the array item size is",mdarray.itemsize,"byte")

reshapearray = mdarray.reshape(3,2)
print(reshapearray)
print("the array dimention is",reshapearray.ndim)
print("the array size is",reshapearray.size)
print("the array shape is",reshapearray.shape)
print("the array item size is",reshapearray.itemsize,"byte")
 

print("the data of slicing is ",mdarray[0,2])
print("the data of slicing is ",mdarray[0:,2])
print("the data of slicing is ",mdarray[1,0:])


# In[23]:


#! python3

import os
import numpy as np
os.system("cls")
mdarray=np.array([[7,8,2,6,9],[3,3,5,4,9],[11,44,88,77,66],[84,24,19,71,65]])
indatarow=int(input("enter the row indexno to find from array "))
print("the data for ",indatarow,"row indexno is \n",mdarray[indatarow,0:])
indatacolumn=int(input("enter the column indexno to find from array "))
print("the data for ",indatacolumn,"column indexno is \n",mdarray[0:,indatacolumn],end="\n")
print("the dimention is ",mdarray.ndim)
print("the itemsize is ",mdarray.itemsize,"bytes")
print("the data type is ",mdarray.dtype)
print("the element size is ",mdarray.size)
print("the shape is ",mdarray.shape)

