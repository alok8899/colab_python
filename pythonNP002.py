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

















