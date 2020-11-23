#! python3

import os


os.system("cls")

"""
def factorials(innumber):
	#Factorial=1
	while innumber>=1:
		Factorial=Factorial*(innumber)
		innumber-=1
	return Factorial

print("the factorial of no ")
invalue=int(input("enter the value to find the factorial : "))

factorials(invalue)
print("the factorial of",factorials(invalue))
"""
"""
def Factorialofnumber(innumber):
	if innumber==0:
		return 1
	else:
		return innumber * Factorialofnumber(innumber-1)

print("the factorial of number ")
infactorialnumber=int(input("enter the value that u want to get factorial : "))
print("the factorial of ",infactorialnumber,"is ",Factorialofnumber(infactorialnumber))
"""

def Factorialofnumber(innumber):
	return 1 if (innumber==0 or innumber==1) else innumber * Factorialofnumber(innumber -1)

factorialinvalue=int(input("enter the value that u want to find factorial : "))
print("the factorial of ",factorialinvalue,"is",Factorialofnumber(factorialinvalue))














































































