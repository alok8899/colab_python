#! python3

import sys

import os
os.system("cls")

maxint=int(sys.maxsize)
minint=int(-sys.maxsize-1)

maxfloat=int(sys.float_info.max)
minfloat=int(-sys.float_info.min)

print("The max size of integer %d"%maxint,end="\n")
print("The min size of integer %d"%minint,end="\n")

print("The max size of float %d"%maxfloat,end="\n")
print("The min size of float %d"%minfloat,end="\n")


