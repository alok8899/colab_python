#!/usr/bin/env python
# coding: utf-8

# In[16]:


#! python3

import os
os.system("cls")

import numpy as np

mdarray=np.linspace(start=0,stop=10)

print("printing the original element\n",end="\n")
print(mdarray)
print(mdarray.size)
print(mdarray.itemsize,"byte")
print(mdarray.shape)

mdarray=np.linspace(start=0,stop=100,num=30)

print("printing the original element\n",end="\n")
print(mdarray)
print(mdarray.size)
print(mdarray.itemsize,"byte")
print(mdarray.shape)


# In[19]:


#! python3

import os
os.system("cls")

import numpy as np

mdarray=np.linspace(start=0,stop=1,num=55)

print("printing the original element\n",end="\n")
print(mdarray)
print(mdarray.size)
print(mdarray.itemsize,"byte")
print(mdarray.shape)


# In[26]:


#! python3

import os
os.system("cls")

import numpy as np

mdarray=np.linspace(start=1,stop=5,num=100,endpoint=False)

print("printing the original element\n",end="\n")
print(mdarray)


# In[33]:


#! python3

import os
os.system("cls")

import numpy as np

mdarray=np.linspace(start=1,stop=5,num=100,dtype=int,endpoint=False)

print("printing the original element\n",end="\n")
print(mdarray)


# In[39]:


# for interval
import numpy as np

mdarray=np.arange(1,10)
print(mdarray)
mdarray=np.arange(10)
print(mdarray)
mdarray=np.arange(1,10,2)#stepup 2
print(mdarray)



# In[3]:


import numpy as np

mdarray=np.arange(10)
print(mdarray)
print(mdarray+.5)
print(mdarray+.25)
print(mdarray+.75)
print(mdarray+5.05)


# In[9]:


import numpy as np

mdarray=np.arange(17)
print(mdarray)
print("after subtract 0.5 from data is \n",mdarray-.5)
print("after subtract 0.25 from data is \n",mdarray-.25)
print("after subtract 0.75 from data is \n",mdarray-.75)
print("after subtract 5.05 from data is \n",mdarray-5.05)

print("after division 0.5 from data is \n",mdarray/.5)
print("after division 0.25 from data is \n",mdarray/.25)
print("after division 0.75 from data is \n",mdarray/.75)
print("after division 5.05 from data is \n",mdarray/5.05)

print("after modulus 0.5 from data is \n",mdarray%.5)
print("after modulus 0.25 from data is \n",mdarray%.25)
print("after modulus 0.75 from data is \n",mdarray%.75)
print("after modulus 5.05 from data is \n",mdarray%5.05)


# In[16]:


# over loading of operator

#! python3

import os
os.system("cls")

import numpy as np

msarray= np.arange(10)
print(msarray)
print("the array is \n")
msarray *=2
print("after multiplaying 2 in each element\n")
print(msarray)
print(sum(msarray))


# In[20]:


#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.arange(1,10).reshape(3,3)
print("the data in array")
print(mdarray)

print("the data of array in transposal format\n")
print(mdarray.T)


# In[26]:


#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.arange(1,10)
print("the data in array")
print(mdarray)

print("the max data of array \n")
print(mdarray.max())

print("the min data of array \n")
print(mdarray.min())


# In[20]:


#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.arange(1,10)
print("the data in array")
print(mdarray)

search=int(input("enter the aray data to search "))
print("searching......search complited ")
surchresult=np.where(mdarray==search)
print(str(surchresult).replace("(array([","the index no is : ").replace("], dtype=int64),)",""))


# In[28]:


# search index no from 
#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.arange(1,22).reshape(3,7)
print("the data in array")
print(mdarray)

search=int(input("enter the aray data to search "))
print("searching......search complited ")
surchresult=np.where(mdarray==search)
print(str(surchresult).replace("(array([","The index no is : ").replace("], dtype=int64), array([",",").replace("], dtype=int64))",""))


# In[35]:






# search index no from 
#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.linspace(start=0,stop=29,num=21).reshape(3,7)
print("the data in array\n")
print(mdarray)

search=int(input("\nenter the aray data to search "))
print("searching......search complited ")
surchresult=np.where(mdarray==search)
print("\n"+str(surchresult).replace("(array([","The index no is : ").replace("], dtype=int64), array([",",").replace("], dtype=int64))",""))


# In[42]:



# indices of element
# search index no from 
#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.arange(1,22).reshape(3,7)
print("the data in array")
print(mdarray)


print("searching......search complited ")
surchresult=np.where(mdarray==np.max(mdarray))
print(surchresult)
print(str(surchresult).replace("(array([","The max index no is : ").replace("], dtype=int64), array([",",").replace("], dtype=int64))",""))


# In[43]:


# indices of element
#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.arange(1,22).reshape(3,7)
print("the data in array")
print(mdarray)


print("searching......search complited ")
surchresult=np.where(mdarray==np.min(mdarray))
print(surchresult)
print(str(surchresult).replace("(array([","The min data index no is : ").replace("], dtype=int64), array([",",").replace("], dtype=int64))",""))


# In[50]:


# indices of element
#! python3

import os
os.system("cls")
import numpy as np
mdarray=np.arange(1,22).reshape(3,7)
print("the data in array")
print(mdarray)

print("\n\nthe data in array after transpose\n")
transposemdarray=mdarray.T
print(transposemdarray)

surchresulttranspose=np.where(transposemdarray==search)

search=int(input("\nenter the aray data to search "))
surchresult=np.where(mdarray==search)

print("searching......search complited ")
print("the index no of '"+str(search)+"' is  ")
print(str(surchresult).replace("(array([","The index no is : ").replace("], dtype=int64), array([",",").replace("], dtype=int64))",""))

print(str(surchresulttranspose).replace("(array([","The index no after transpose is : ").replace("], dtype=int64), array([",",").replace("], dtype=int64))",""))


# In[56]:


#row wise highest element
# axis 0=column (X axis)
# axis 1=row (Y axis)

#! python3
import os
os.system("cls")

import numpy as np

mdarray=np.arange(5,45).reshape(8,5)
print(mdarray)
print("The max element in row wise is : ",mdarray.max(axis=1))
print("The min element in row wise is : ",mdarray.min(axis=1))
print("\n")

print("The max element in column wise is : ",mdarray.max(axis=0))
print("The min element in column wise is : ",mdarray.min(axis=0))



# In[6]:


# indices of element
#! python3
import os
os.system("cls")

import numpy as np
mdarray=np.array([[ 5 , 6 , 2 , 8 , 1],[10 ,11 ,10 ,13 ,18],[15, 12, 17, 1 ,3],
 [20 ,21 ,22 ,2 ,7],
 [25 ,99 ,27 ,28 ,9],
 [75 ,31 ,32 ,33 ,4],
 [35 ,99 ,37 ,38 ,8],
 [40 ,77 ,42 ,77 ,44]])

print("the element of array is \n",mdarray,end="\n\n")
print("the element of array after transpose\n",mdarray.T,end="\n")

print("the max element of normal array is ",np.max(mdarray))

print("the index no for the max no in normal array is ",np.where(mdarray==np.max(mdarray)))
print("the index no for the max no in normal array is ",np.where(mdarray.T==np.max(mdarray.T)),end="\n")

print("the largest element in row wise ",mdarray.max(axis=1))
print("the largest element in colmn wise ",mdarray.max(axis=0),end="\n")

print("the smalest element in row wise ",mdarray.min(axis=1))
print("the smalest element in column wise ",mdarray.min(axis=0))

print("the largest element in row wise in transpose aray ",mdarray.T.max(axis=1))
print("the largest element in colmn wise in transpose aray ",mdarray.T.max(axis=0),end="\n")

print("the smalest element in row wise in transpose aray ",mdarray.T.min(axis=1))
print("the smalest element in column wise in transpose aray ",mdarray.T.min(axis=0))


# In[14]:


#find the INDEX NO OF MAX OR MIN VALUE 
#! python3

import os 
os.system("cls")

import numpy as np
mdarray=np.array([[ 5 , 6 , 2 , 8 , 1],[10 ,11 ,10 ,13 ,18],[15, 12, 17, 1 ,3],
 [20 ,21 ,22 ,2 ,7],
 [1 ,99 ,27 ,28 ,9],
 [75 ,1 ,32 ,33 ,4],
 [35 ,99 ,37 ,4 ,8],
 [40 ,77 ,42 ,77 ,44]])

print("\nthe element of array\n",mdarray)
print("\nthe element in max value in row wise ",mdarray.max(axis=1))
print("\nthe index no of max value in row wise ",np.argmax(mdarray,axis=1))
print("\nthe element in min value in row wise ",mdarray.min(axis=1))
print("\nthe index no of min value in row wise ",np.argmin(mdarray,axis=1))

print("---------------------------------------------------------------")
print("\nthe element in max value in column wise ",mdarray.max(axis=0))
print("\nthe index no of max value in column wise ",np.argmax(mdarray,axis=0))
print("\nthe element in min value in column wise ",mdarray.min(axis=0))
print("\nthe index no of min value in column wise ",np.argmin(mdarray,axis=0))



# In[23]:


#! python3

import os
os.system("cls")

import numpy as np
mdarray=np.array([[ 5 , 6 , 2 , 8 , 1],[10 ,11 ,10 ,13 ,18],[15, 12, 17, 1 ,3],
 [20 ,21 ,22 ,2 ,7],
 [1 ,99 ,27 ,28 ,9],
 [75 ,1 ,32 ,33 ,4],
 [35 ,99 ,37 ,4 ,8],
 [40 ,77 ,42 ,77 ,44]])

print("the element of array is\n",mdarray,end="\n\n")
print("the sum of element on row wise : ",mdarray.sum(axis=1))
print("the sum of element on column wise : ",mdarray.sum(axis=0))

print("the sum of all element : ",np.sum(mdarray))
print("the cumulative sum of all element or array : ",mdarray.cumsum())
print("the cumulative sum of element on row wise : \n",mdarray.cumsum(axis=1))
print("the cumulative sum of element on column wise : \n",mdarray.cumsum(axis=0))





# In[29]:


#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5]])
secondarray= np.array([[70,4,2,1],[3,6,1,68],[89,26,32,54]])

print("the element of fast array is \n",fastarray)
print("the element of second array is \n",secondarray)

combinearray=fastarray + secondarray
print("the element after join two array is \n",combinearray)
suntractarray=fastarray - secondarray
print("the element after substract second array from fast array is \n",suntractarray)




# In[31]:


# array multiplication

#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5]])
secondarray= np.array([[70,4,2,1],[3,6,1,68],[89,26,32,54]])

multiplicationarray=fastarray*secondarray
print("the fast array\n",fastarray)
print("the second array\n",secondarray)
print("the multiplication of array is \n",multiplicationarray)


# In[37]:


# matrix multiplication 
# use n x n matrix 
#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5],[1,1,1,1]])
secondarray= np.array([[70,4,2,1],[3,6,1,68],[89,26,32,54],[1,1,1,1]])


print("the fast array\n",fastarray)
print("the second array\n",secondarray)
print("the matrix multiplication is ",fastarray.dot(secondarray))


# In[39]:


# sin value 

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5],[1,1,1,1]])

print("the element of array is \n",fastarray)
print("the sin value of matrix is \n",np.sin(fastarray))


# In[42]:


# exponnanttial 

#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5],[1,1,1,1]])

print("the element of array is \n",fastarray)

print("the expnantial data is \n",np.exp(fastarray))


# In[43]:


# square root valu
#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5],[1,1,1,1]])

print("the element of array is \n",fastarray)

print("the squareroot data is \n",np.sqrt(fastarray))


# In[44]:


# standard deviation
#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5],[1,1,1,1]])

print("the element of array is \n",fastarray)

print("the standard deviation data is \n",np.std(fastarray))


# In[46]:


# concat vartically two string

#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5],[1,1,1,1]])
secondarray= np.array([[70,4,2,1],[3,6,1,68],[89,26,32,54],[1,1,1,1]])


print("the fast array is\n",fastarray)
print("the second array is\n",secondarray)

print("the concatination of string is \n",np.vstack((fastarray,secondarray))) #vartically concat


# In[47]:


# concat horizentally two string

#! python3

import os
os.system("cls")

import numpy as np
fastarray= np.array([[90,43,22,51],[34,66,41,38],[9,6,2,5],[1,1,1,1]])
secondarray= np.array([[70,4,2,1],[3,6,1,68],[89,26,32,54],[1,1,1,1]])


print("the fast array is\n",fastarray)
print("the second array is\n",secondarray)

print("the concatination of string is \n",np.hstack((fastarray,secondarray))) #vartically concat


# In[21]:


import numpy
dir(numpy)

