#!/usr/bin/env python
# coding: utf-8

# In[44]:


#! python3
# > big endian notation
# < little endian notation

import os
os.system("cls")

import numpy as np
ff=np.array([[1,4],[8,7],[88,7]])
mydatatype=np.dtype('>i4')
print("the byte order of the data type is ",mydatatype.byteorder)
print("the size of datatype is ",mydatatype.itemsize)
print("the data type is ",mydatatype.name)
print("the calass of data type ",type(mydatatype))

