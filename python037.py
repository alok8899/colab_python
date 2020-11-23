#! python3


import os
os.system("cls")
import time


def datainput():
	print("\nPlease wait................",end="\n")
	print("processing................",end="\n")
	time.sleep(2)

	actfname=input("enter the fast name:- ")
	actmname=input("enter the middle name:- ")
	actlname=input("enter the last name:- ")
	
	print("\nPlease wait................",end="\n")
	print("Inserted data is processing................",end="\n")
	time.sleep(2)
	dataprint(actfname,actmname,actlname)
	time.sleep(2)
	return


def dataprint(forfname,formname,forlname):
	print("the entered data is.......")
	print("the 1st name is ",forfname)
	print("the mid name is ",formname)
	print("the last name is ",forlname)

	time.sleep(1)
	conform=input("do u want to print fullname pls type Y or N ")
	if conform=="y" or conform=="Y":
		print("the full name is",forfname,formname,forlname)
	elif conform=="n" or conform=="N":
		print("ok")
	else:
		print("please enter proprer word Y or N")
	time.sleep(2)
	print("the data print completed")
	return

print("welcome to customer name portal")
time.sleep(2)
datainput()









