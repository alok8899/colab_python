#! python3

from os import system


"""
set1={'cricket','foot ball','swimmin',1,2}

print(type(set1))
print(set1)


# set don't have append because it doesn't have any index
set1={'cricket','foot ball','swimmin',1,2}
set1.add('hocky')
print("after append the set is ",set1)

newset=set()
loopcount=True
while loopcount:
	insertdata=input("\nenter the frut name to add into set :- ")
	newset.add(insertdata)
	conform=input("\ndo u want to continue (Y or N) :  ")
	if conform=='Y' or conform=='y':
		loopcount=True
	elif conform=='N' or conform=='n':
		print("\n thanks for replay")
		loopcount=False
	else:
		print("enter proper data")
for indexno in newset:
	print("\n",indexno)
"""

"""
blankset=set()
inrange1=int(input("enter the fast range "))
inrange2=int(input("enter the second range "))
for loopindex in range(inrange1,inrange2):
	blankset.add(loopindex)
print(blankset)
"""
"""
#it does not take duplicate data
blankset={'cricket','Cricket','cricket','base ball','tiger','cricket'}
print("the data on set is\n",blankset)

searchdata=input("enter the data you want to search : ")

print("please wait search completed")
if searchdata in blankset:
	blankset.remove(searchdata)	
	print("the data on set is\n",blankset)
else:
	print("the data '"+str(searchdata)+"' is not in the set")
"""
"""
blankset1=set()
blankset2=set()
loopstate=True
while loopstate:
	dataforset1=input("please insert data for vegitable:- ")
	blankset1.add(dataforset1)
	conform=input("do you want to add data to set1 (Y or N) :- ")
	if conform=='Y' or conform=='y':
		loopstate=True
	else:
		loopstate=False

loopstate=True
while loopstate:
	dataforset2=input("please insert data for fruts:- ")
	blankset2.add(dataforset2)
	conform=input("do you want to add data to set2 (Y or N) :- ")
	if conform=='Y' or conform=='y':
		loopstate=True
	else:
		loopstate=False
print("the data on vegitable is\n",blankset1)
print("the data on fruts is\n",blankset2)

finalcart=set(blankset1.union(blankset2))
print("the data in your cart is ",finalcart)
"""
"""
blankset1=set()
blankset2=set()
loopstate=True
while loopstate:
	dataforset1=input("please insert data for vegitable:- ")
	blankset1.add(dataforset1)
	conform=input("do you want to add data to set1 (Y or N) :- ")
	if conform=='Y' or conform=='y':
		loopstate=True
	else:
		loopstate=False
print("the data on vegitable is\n",blankset1)

loopstate=True
while loopstate:
	dataforset2=input("please insert data for fruts:- ")
	blankset2.add(dataforset2)
	conform=input("do you want to add data to set2 (Y or N) :- ")
	if conform=='Y' or conform=='y':
		loopstate=True
	else:
		loopstate=False

print("the data on fruts is\n",blankset2)

finalcart=set(blankset1|blankset2)
print("the data in your cart is \n",finalcart)
"""
"""
#system("cls")
#having 2 list how to get common element from 2 list
list1=['cricket','football','cricket','cricket','volly ball','cricket']
list2=['football','swimming','swimming','football','football','running','football']
#commondata=set(set(list1)&set(list2))
commondata=set(set(list1).intersection(set(list2)))

#alldata=set(set(list1)|set(list2))
alldata=set(set(list1).union(set(list2)))

#minusofset1=set(set(list1)-set(list2))
minusofset1=set(set(list1).difference(set(list2)))
#for this case difference is (A - B)

#minusofset2=set(set(list2)-set(list1))
minusofset2=set(set(list2).difference(set(list1)))
#for this case difference is (B - A)


#minusofboth=set(set(list1).symmetric_difference(set(list2)))
minusofboth=set(set(list1)^(set(list2)))
#symmetric_difference  = (A - B) union (B - A)




print(list1)
print(list2)
print("common data is \n",commondata)
print("all data is \n",alldata)
print("minus data of 1st set \n",minusofset1)
print("minus data of 2nd set \n",minusofset2)
print("minus data is \n",minusofboth)

"""
"""
#to find a string inside set
set1={'cricket','football','cricket','cricket','volly ball','cricket'}
print(set1) 
set1.discard('crick')
set1.remove('crick')

print(set1)
"""
"""
#if the set disjoint return true

set1={'cricket','football','cricket','cricket','volly ball','cricket'}

set2={'swiming','weight lift','running'}

set3={'cricket','table tenish'}
print(set1)
print(set2)
print(set3)
#means it doesnot have common element
print("the isdisjoin on set1 and set2 is: ",set1.isdisjoint(set2))
print("the isdisjoin on set1 and set3 is: ",set1.isdisjoint(set3))

#subset all the data of set1 is present on set2 
print("the isdisjoin on set1 and set2 is: ",set1.issubset(set2))
print("the isdisjoin on set1 and set3 is: ",set1.issubset(set3))

#superset all data of set2 is belong to set1
print("the isdisjoin on set1 and set2 is: ",set1.issuperset(set2))
print("the isdisjoin on set1 and set3 is: ",set1.issuperset(set3)) 
"""

set1={'cricket','football','cricket','cricket','volly ball','cricket'}
print(type(set1))

print(type(sorted(set1)))

print(sorted(set1))
print(type(set1))



















