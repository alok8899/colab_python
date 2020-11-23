"""
list1=['cricket','cricket','football','Cricket']
print(list1)
delobject=input("please insert the object that to be delete :- ")
countstr=list1.count(delobject)
if countstr>0:
	print("your searching element '"+delobject+"' is found")
	conform=input("do u want to delete data from list (Y or N)  ")
	if conform=='Y' or conform=='y':
		loopcount=1
		while loopcount<=countstr:
			list1.remove(delobject)
			loopcount+=1
else:
	print("you insert wrong objet data for the list")
print(list1)
"""
"""
list1=['cricket','cricket','football','Cricket']
print(list1)
delobject=input("please insert the object that to be delete :- ")
countstr=list1.count(delobject)
if delobject in list1:
	print("your searching element '"+delobject+"' is found")
	conform=input("do u want to delete data from list (Y or N)  ")
	if conform=='Y' or conform=='y':
		loopcount=1
		while loopcount<=countstr:
			list1.remove(delobject)
			loopcount+=1
else:
	print("you insert wrong objet data for the list")
print(list1)
"""
"""
list1=['cricket','cricket','football','Cricket']
list2=list1
print("list1 := ",list1)
print("list2 := ",list2)
print("going to append on list2 ")
list2.append('alok')
print("list2 := ",list2)
print("list1 := ",list1)

" when a list is direct assigned to another list (copyed list) then append operation in copped list then original list affect in append because both list share same momory location"

"""
"""
list1=['cricket','cricket','football','Cricket']
list2=list1.copy()
print("list1 := ",list1)
print("list2 := ",list2)
print("going to append on list2 ")
list2.append('alok')
print("list2 := ",list2)
print("list1 := ",list1)

" when a list is assigned by coppy method to another list (copyed list) then append operation in copped list then original list is not affect in append because  list have different momory location"

"""
"""
list1=['cricket','cricket','football','Cricket']
list2=list1[:]
print("list1 := ",list1)
print("list2 := ",list2)
print("going to append on list2 ")
list2.append('alok')
print("list2 := ",list2)
print("list1 := ",list1)
"""
"""
list1=['cricket','cricket','football','Cricket','jhjjbj','nnnjnjn']
list2=list1[2:4]
print("list1 := ",list1)
print("list2 := ",list2)
print("going to append on list2 ")
list2.append('alok')
print("list2 := ",list2)
print("list1 := ",list1)
"""
"""
list1=['cricket','cricket','football','Cricket','baseball','hocky']
print(list1)
print("After clear from list")
list1.clear()
print(list1)
"""
"""
list1=['cricket','cricket','football','Cricket','baseball','hocky']
print(list1)
print("After clear from list")
list2=enumerate(list1)
print(list2)
print(list(list2))
"""
"""
list1=['cricket','cricket','football','Cricket','baseball','hocky']
for spotitem in list1:
	print("the value for list is",spotitem)
print("\nthe total element in the list by enumerator value")
print("the data in tabular form")
print("\t","index_no","\t","spot_name")
print("\t----------\t-----------")
for spotnumber,spotitem in list(enumerate(list1,10)):
	print("\t",spotnumber,"\t\t",spotitem)
"""
list1=['cricket','football','polo','swimming','baseball','hocky']





































































































































































































































































