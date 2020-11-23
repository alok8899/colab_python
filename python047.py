#! python3


import os
os.system("cls")

"""

listsport=['cricket','voley','bad minton','base ball']
print("\nThe sport list index 0: ",listsport[0])
print("\nThe sport list index 1: ",listsport[1])
print("\nThe sport list index 2: ",listsport[2])
print("\nThe sport list index 3: ",listsport[3])

"""

"""
listage=[10,85,45,78,15]
print("\n the age is: ",listage[0])
print("\n the age is: ",listage[1])
print("\n the age is: ",listage[2])
print("\n the age is: ",listage[3])
print("\n the age is: ",listage[4])

"""

"""
listage=[10,85,45,78,15]

print("\nThe original eliment is: ",list(listage))
print("\nThe slicing of element is[3:5]",listage[3:5])
print("\nThe slicing of element is[:3]",listage[:3])

"""

"""
" slicing in runtime "

listnum=[10,85,45,13,45,78,40,53]

loopstate=True
while loopstate:

	os.system("cls")
	print("\nThe original eliment is: ",list(listnum))
	sliceposition=int(input("\nenter the position for slicing : "))
	noofposition=int(input("\nenter the no to slicing : "))
	print("\nyou see the slicing value of  [",sliceposition,":",(sliceposition+noofposition),"]")
	print("\n The final sliced value is : ",listnum[sliceposition:(sliceposition+noofposition)])
	continuestatus=input("\nIf you want to continue type \"Y\" or \"N\"")
	if continuestatus=='Y' or continuestatus=='y':
		loopstate=True
	elif continuestatus=='N' or continuestatus=='n':
		loopstate=False

	else:
		print("enter proper input")

"""
"""
" updating list data "

mylist=['cricket','base ball','hocky','table tenis','jumping','running','swiming']
print("\n",list(mylist))

uvalue=int(input("\nenter the index no in where u want to update "))

if uvalue<len(mylist) and  uvalue>0:

	udata=input("\nenter the data that u want to update ")

	mylist[uvalue]=udata
	print("\nthe data is updated sucessfully... ")
	print("\nthe data after update  \n",mylist)
else:
	print("\nthe entered index is not valid")

"""

"""
" delete list data "

mylist=['cricket','base ball','hocky','table tenis','jumping','running','swiming']
print("\n",list(mylist))

delval=int(input("\nenter the index no which u want to delete "))

if delval<len(mylist) and  delval>0:

	print("\nthe the index value is ",mylist[delval])
	conform=input("\nare you confot=rm to delete Y or N  ")
	if conform=='Y' or conform=='y':

		del mylist[delval]
		print("\nthe data after delete")
		print("\n",list(mylist))
else:
	print("\nyour index no is invalid ")
print("\nthanks for executing the code")

"""














