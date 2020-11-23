#! python3

from os import system


system("cls")
"""
list1=[1,2,3,'e',29.4]
tuple1=(1,2,3,'e',29.4)
print(list1)
print(tuple1)
list1
tuple1

print(list1[0])
print(tuple1[0])


tuple2=('mango','banana','pinaple','bread')

for indexno in tuple2:
	 print("the index no '"+str(tuple2.index(indexno))+"' the data is ",indexno)
list3=[1,7,25,18,2,74,3]
tuple3=(1,7,25,18,2,74,3)

print(list3[1:3])

list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

ftuple3=tuple(sorted(tuple3))
print(ftuple3)
ftuple3=tuple(sorted(tuple3,reverse=True))
print(ftuple3)
print(type(ftuple3))
"""
"""
tuplelist=('cricket','football','volly')
for indexno in tuplelist:
	print("the data for tuple in '"+str(tuplelist.index(indexno))+"' is ",indexno)
print(type(tuplelist))
inindexno=int(input("enter the index no that to update"))
print("the '"+str(inindexno)+"' data is ",tuplelist[inindexno])
prompt1="enter the data to insert in index no '"+str(inindexno)+"'  "
indata=input(prompt1)

tuplelist=list(tuplelist)
tuplelist[inindexno]=indata
print(type(tuplelist))
tuplelist=tuple(tuplelist)

for indexno in tuplelist:
	print("the data for tuple in '"+str(tuplelist.index(indexno))+"' is ",indexno)


print(type(tuplelist))
"""
tuplelist=('cricket','football','volly','baseball','football','j')
for indexno in tuplelist:
	print("the data of taple index '"+str(tuplelist.index(indexno))+"' is :- ",indexno)
inindexdata=input("enter the data to delete")
countinindexdata=int(tuplelist.count(inindexdata))
tuplelist=list(tuplelist)
if countinindexdata>0:
	for x in range(1,countinindexdata+1):
		tuplelist.remove(inindexdata)

tuplelist=tuple(tuplelist)

for indexno in tuplelist:
	print("the data of taple index '"+str(tuplelist.index(indexno))+"' is :- ",indexno)



























































































