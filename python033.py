#! python3

import os
os.system("cls")


instring1=input("please enter a string:- ")


#isalpha
if instring1.isalpha()== True:
	print("the string contain alphabet ")
else:
	print("the string contain alphabet with number and  space and spacial character")


#isdecimal no need to convert to float
#value1=input("enter the float value")
if ("\u00B2".isdecimal()== True):
	print("the data is decimal ")
else:
	print("the data is not not decimal")


#isdigit no need to convert int
#age=input("enter the age")
if ("\u00B2".isdigit()== True):
	print("the data is digit ")
else:
	print("the data is not not digit")








