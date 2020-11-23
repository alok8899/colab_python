"""
mylist=['alok','kumar','behera',9437094370,'alok.behera.1992@gmail.com',36,5.6]

print(mylist)
print("\ncustomer name ",mylist[0:3])
print("\ncustomer mob & email ",mylist[3:5])
print("\ncustomer age& haight ",mylist[5:7])

print("customer fast name ",mylist[0])
print("customer mid name ",mylist[1])
print("customer last name ",mylist[2])
print("customer mob no ",mylist[3])
print("customer email id ",mylist[4])
print("customer age ",mylist[5],"year")
print("customer heaight ",mylist[6]," ft")
"""
"""
mylist=[['alok','kumar','behera'],[9437094370,'alok.behera.1992@gmail.com'],[36,5.6]]

print(mylist)
print("\ncustomer name ",mylist[0])
print("\ncustomer mob & email ",mylist[1])
print("\ncustomer age& haight ",mylist[2])

print("customer fast name ",mylist[0][0])
print("customer mid name ",mylist[0][1])
print("customer last name ",mylist[0][2])
print("customer mob no ",mylist[1][0])
print("customer email id ",mylist[1][1])
print("customer age ",mylist[2][0],"year")
print("customer heaight ",mylist[2][1]," ft")
"""

"""
mylist=[['alok',['kumar','behera']],[9437094370,['alok.behera.1992@gmail.com']],[36,[5.6]]]

print(mylist)
print("\ncustomer name ",mylist[0])
print("\ncustomer mob & email ",mylist[1])
print("\ncustomer age& haight ",mylist[2])

print("customer fast name ",mylist[0][0])
print("customer mid name ",mylist[0][1][0])
print("customer last name ",mylist[0][1][1])
print("customer mob no ",mylist[1][0])
print("customer email id ",mylist[1][1][0])
print("customer age ",mylist[2][0],"year")
print("customer heaight ",mylist[2][1][0]," ft")

"""
"""
list1=['cricket','foot ball','shuttle','base ball']
list2=['handball','kabadi','swimming']
loopcount=0

for x in list1:

	print("\n For index in list1 ",loopcount,"is : ",x)
	loopcount = loopcount +1
print("\n\n")
loopcount=0
for x in list2:

	print("\n For index in list2 ",loopcount,"is : ",x)
	loopcount = loopcount +1
print("\n\n")
print("\nNow merging of two string.....")
loopcount=0
finallist = list1 + list2
for x in finallist:

	print("\n For index in finallist ",loopcount,"is : ",x)
	loopcount = loopcount +1
	
"""
"""
list1=['cricket','foot ball','shuttle','base ball','kabadi']
list2=['handball','kabadi','swimming','foot ball']

print("\n",list1)
print("\n",list2)
finallist=list1+list2
print("\nfinal list after merging")
print("---------------------------\n")
print(finallist)

cstring=input("\n please give the index no in which u want to search how many ocurance present ")
upperfinallisa=[i.upper() for i in finallist] 

print("\nthe count of ",cstring," for is ",upperfinallisa.count(cstring.upper()))

print(upperfinallisa)

"""

"""
cart= []

print("the item is availabel for sell")
print("1.    Banana")
print("2.    Pinaple")
print("3.    Orange")
print("4.    Apple")
print("5.    Jack frut")
print("6.    Naspati")
print("7.    Guava")
print("8.    Chery")

loopstaus=True
while loopstaus:


	uchoice=input("\n Please enter the choice(0 to Exit) :   ")
	
		


	if int(uchoice)>0 and int(uchoice)<9:
		

		if int(uchoice)==1:
			cart.append("Banana")

		elif int(uchoice)==2:
			cart.append("Pinaple")

		elif int(uchoice)==3:
			cart.append("Orange")

		elif int(uchoice)==4:
			cart.append("Apple")

		elif int(uchoice)==5:
			cart.append("Jack frut")

		elif int(uchoice)==6:
			cart.append("Naspati")

		elif int(uchoice)==7:
			cart.append("Guava")

		elif int(uchoice)==8:
			cart.append("Chery")
	elif not uchoice:
		loopstaus=False

	else:
		loopstaus=False 
		

print("the iteam on cart is")
print(cart)

"""

"""

list1=['cricket','foot ball','vally ball','table tenish','hocky','running','swimming']

print(list1)

print(" the list of sport available")
print("-----------------------------")

loopcount=0
while (loopcount < len(list1)):
	print(loopcount+1,"  .  ",list1[loopcount])
	loopcount=loopcount+1
myprompt="\n Please input the choice( 1 to "+str(len(list1))+") : "

inchoice=int(input(myprompt))

if inchoice==1:
	print("\n\nthe selected choice is '"+list1[inchoice-1]+"'")


elif inchoice==2:
	print("\n\nthe selected choice is '"+list1[inchoice-1]+"'")

elif inchoice==3:
	print("\n\nthe selected choice is '"+list1[inchoice-1]+"'")

elif inchoice==4:
	print("\n\nthe selected choice is '"+list1[inchoice-1]+"'")

elif inchoice==5:
	print("\n\nthe selected choice is '"+list1[inchoice-1]+"'")

elif inchoice==6:
	print("\n\nthe selected choice is '"+list1[inchoice-1]+"'")

elif inchoice==7:
	print("\n\nthe selected choice is '"+list1[inchoice-1]+"'")

else:
	print("\n\n Going to fire uuuuuuu.....")
	exit()
print("\n Y R WELLCOME.....")

"""
"""
list1=[1,4,55,7,22,555,111]


print(" the list of sport available")
print("-----------------------------")

loopcount=0
while (loopcount < len(list1)):
	print(loopcount+1,"  .  ",list1[loopcount])
	loopcount=loopcount+1

print("\n\nthe max of list is ",max(list1),len(list1))
print("\nthe min of list is ",min(list1))

"""
"""
mylist=[]
Value=int(input("\nPls type how many data u want to insert : "))
print("\n\n")
for i in range(0,Value):
	indata=input("enter the data for '"+str(i+1)+"' - ")
	mylist.append(indata)
print("\n\nThe output is ",mylist)

"""
"""
mylist=[]
Value=int(input("\nPls type how many data u want to insert : "))
print(" please don't add duplicate data")
print("\n\n")
for i in range(0,Value):
	indata=input("enter the data for '"+str(i+1)+"' - ")
	mylist.append(indata)
print("\n\nThe output is ",mylist)
"""
import os
os.system("cls")
"""
list1=['cricket','foot ball','shuttle','base ball','cricket','kabadi']
list2=['handball','kabadi','cricket','swimming','foot ball']


print(list1)

print(list2)
print("\n\n")
print("append of two list")
list1.append(list2)
print(list1)
print("\n\n")
print("append of list with one object")
list2.append('xxx')
print(list2)

"""
"""
list1=['cricket','foot ball','shuttle','base ball','cricket','kabadi']
list2=['handball','kabadi','cricket','swimming','foot ball']

print(list1)
print("\n\n")
print(list2)
list1.extend(list2)
print("\n",list1)
list2.extend("alok")
print("\n",list2)

"""
"""
list1=['cricket','foot ball','shuttle','base ball','cricket','kabadi']
print(list1)
search1=input("enter the string to search :- ")
list3=[i.upper() for i in list1]
print(list3.count(search1))
"IF THE GIVEN STRING IS PRESENT IN THE LIST THEN COUNT GIVES NO TOMES IT PRESENT(NUMARIC).. IF NOT PRESENT IT GIVES ZERO IT DOES NOT GIVE ANY ERROR"
"IF THE GIVEN STRING IS PRESENT IN THE LIST THEN INDEX GIVES THE INDEX NO IF NOT THEN IT GIVES AN ERROR"
print(list3.index(search1))

"""
"""
list1=['cricket','foot ball','shuttle','base ball','cricket','kabadi']
print(list1,end="\n")
print("the data on list in serialy")
loopcount=0
while loopcount<len(list1):
	print("the index of '"+str(loopcount)+"' is :- '"+list1[loopcount]+"'")
	loopcount=loopcount+1
conform=input("Do u want to add data into the list (Y or N):  ")

if conform=='Y' or conform=='y':
	posi=int(input("\nenter the position of index in where u want to add :- "))
	prompt1="enter the string u want to add in positino "+str(posi)+" is :- "
	strin=input(prompt1)

	list1.insert(posi,strin)

	print("the data after add in '"+str(posi)+"' position")
	loopcount=0
	while loopcount<len(list1):
		print("the index of '"+str(loopcount)+"' is :- '"+list1[loopcount]+"'")
		loopcount=loopcount+1
"""	
"""
list1=['cricket','foot ball','shuttle','base ball','cricket','kabadi']
loopcont=0
while loopcont<len(list1):
	print("The data in index '"+str(loopcont)+"' is :- "+str(list1[loopcont])+"")
	loopcont+=1
indexno=int(input("please input the index no for which u want to pop : "))

if indexno<len(list1) and indexno>=0:
	Prompt="do u want to pop '"+str(indexno)+"' index from list (Y or N) :-  "
	inputconform=input(Prompt)
	if inputconform=='Y' or inputconform=='y':

		list1.pop(indexno)
		loopcont=0
		while loopcont<len(list1):
			print("The data in index '"+str(loopcont)+"' is :- "+str(list1[loopcont])+"")
			loopcont+=1
	
else:
	print("the index is not in range (0 to "+str(len(list1))+")")
 
"""
"""
list1=['cricket','foot ball','shuttle','base ball','cricket','kabadi']
loopstate=0
while loopstate<len(list1):
	print("the data of index no '"+str(loopstate)+"' is :- ",list1[loopstate])
	loopstate+=1

conform=input("do u want to reverse the data on list (Y or N) : ")
if conform=='Y' or conform=='y':
	list1.reverse()

	loopstate=0
	while loopstate<len(list1):
		print("the data of index no '"+str(loopstate)+"' is :- ",list1[loopstate])
		loopstate+=1
"""

"""
#list1=['cricket','foot ball','shuttle','base ball','cricket','kabadi']
list1=[1,78,2,14]

loopstate=0
while loopstate<len(list1):
	print("the data of index no '"+str(loopstate)+"' is :- ",list1[loopstate])
	loopstate+=1

conform=input("do u want to short the data on list (Y or N) : ")
if conform=='Y' or conform=='y':
	list1.sort(reverse=True)
	#list1.sort()
	loopstate=0
	while loopstate<len(list1):
		print("the data of index no '"+str(loopstate)+"' is :- ",list1[loopstate])
		loopstate+=1
print(list1)

"""

fastname=input("enter a string to convert a string to list :- ")
fastname=list(fastname)
print(fastname)
conform=input("do u want to delete the data on list (Y or N) : ")
if conform=='Y' or conform=='y':
	indexno=input("enter the object name that u want to delete")
	fastname.remove(indexno)
print(fastname)
















