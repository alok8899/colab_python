#! python3

import os
os.system("cls")

def sumation(innumber):
	return 0 if (innumber<0) else innumber + sumation(innumber-1)
inputvalue=int(input("enter the value u want to sum from 1 is : - "))
print("the o/p of ",inputvalue," sum is ",sumation(inputvalue))




















