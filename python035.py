#! python3


import os
os.system("cls")

import time

# start of function  diclaration

def myfun1():
	print("begning of myfun1")
	time.sleep(0.5)
	print("inside myfun1")
	myfun2()
	print("after calling myfun2 inside myfun1")
	time.sleep(2)
	return

def myfun2():
	print("you are in side myfun2")
	time.sleep(3)
	
	return
#end of function declaration

"""end of function declaartion"""

time.sleep(3)
print("you are going to see magic")
time.sleep(2)
myfun1()
time.sleep(2)
myfun2()
time.sleep(2)
print("end of the function")
