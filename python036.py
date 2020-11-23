#! python3


import os
os.system("cls")
""" function not accepting parameter and nor returning value """
"""-------------------------------------------------------------"""

"""
def addvalue():
	val1fun1=int(input("enter 1st value : "))
	val2fun1=int(input("enter 2nd value : "))
	outputvalue=val1fun1+val2fun1
	print("the result is ",outputvalue)
	return

addvalue()

"""


""" function not accepting parameter and returning value """
"""-------------------------------------------------------------"""

"""
def addvalue():
	val1fun1=int(input("enter 1st value : "))
	val2fun1=int(input("enter 2nd value : "))
	outputvalue=val1fun1+val2fun1
	return outputvalue 


resultvalue=addvalue()
print("the result is ",resultvalue)

"""

""" function accepting parameter and not returning value """
"""-------------------------------------------------------------"""

"""
def addvalue(formal1fun1,formal2fun1):

	outputvalue=actual1fun1+actual2fun1
	print("the result is ",outputvalue)
	return 
	


actual1fun1=int(input("enter 1st value : "))
actual2fun1=int(input("enter 2nd value : "))
addvalue(actual1fun1,actual2fun1)


"""


""" function accepting parameter and returning value """
"""-------------------------------------------------------------"""

def addvalue(formal1fun1,formal2fun1):

	outputvalue=actual1fun1+actual2fun1
	return outputvalue
	


actual1fun1=int(input("enter 1st value : "))
actual2fun1=int(input("enter 2nd value : "))
result=addvalue(actual1fun1,actual2fun1)
print("the result is ",result)



