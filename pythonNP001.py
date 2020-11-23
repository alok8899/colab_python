
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
 
print(mdarray)
print("the data of slicing is ",mdarray[0,2])
print("the data of slicing column is ",mdarray[0:,2])
print("the data of slicing row is ",mdarray[1,0:])
print("the data of slicing row with column is \n",mdarray[0:,1:])

mdarray=np.array([[7,8,2,6,9],[3,3,5,4,9],[11,44,88,77,66],[84,24,19,71,65]])
indatarow=int(input("enter the row indexno to find from array "))
print("the data for ",indatarow,"row indexno is \n",mdarray[indatarow,0:])
indatacolumn=int(input("enter the column indexno to find from array "))
print("the data for ",indatacolumn,"column indexno is \n",mdarray[0:,indatacolumn])
































































