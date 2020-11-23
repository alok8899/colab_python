#! python3

import os
os.system("cls")
import time

def myfun():
	""" inside function"""
	time.sleep(1)
	print("insise function")
	time.sleep(0.5)
	return
time.sleep(1)
print("out side of function")

myfun()

print("2nd outside")
time.sleep(0.1)
myfun()








