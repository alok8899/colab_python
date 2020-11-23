#! python3


import os
os.system("cls")

#function declaration start

def addfun(formalval01,formalval02):
	addresult=formalval01+formalval02
	return addresult


def subfun(formalval01,formalval02):
	subresult=formalval01-formalval02
	return subresult

def mulfun(formalval01,formalval02):
	mulresult=formalval01*formalval02
	return mulresult

def divfun(formalval01,formalval02):
	divresult=formalval01-formalval02
	return divresult

def thanks():
	print("         THANKS  You")
	return

#end function declaration


invalue1=int(input("enter first value : "))
invalue2=int(input("enter second value : "))

print("     type 1:- ADDITION")
print("     type 2:- SUBTRACTION")
print("     type 3:- MULTIPLICATION")
print("     type 4:- DIVISION")


choice=int(input("                       enter your choice : "))
if choice==1:
	addfun(invalue1,invalue2)
	result=addfun(invalue1,invalue2)
	print("the add of",invalue1,"and",invalue2,"is:-  ",result)
	thanks()

elif choice==2:
	subfun(invalue1,invalue2)
	result=subfun(invalue1,invalue2)
	print("the sub of",invalue1,"and",invalue2,"is:-  ",result)
	thanks()

elif choice==3:
	mulfun(invalue1,invalue2)
	result=mulfun(invalue1,invalue2)
	print("the mul of",invalue1,"and",invalue2,"is:-  ",result)
	thanks()

elif choice==4:
	divfun(invalue1,invalue2)
	result=divfun(invalue1,invalue2)
	print("the div of",invalue1,"and",invalue2,"is:-  ",result)
	thanks()

else:
	print("          I going to fire you")

