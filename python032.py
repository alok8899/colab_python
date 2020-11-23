#! python3


import os
os.system("cls")




instring1=input("enter a string :- ")
print("----------------",end="\n\n\n")


print("The o/p in capitalize:- ",instring1.capitalize(),end="\n")

print("The o/p in center:- ",instring1.center(20,"-"),end="\n")

print("The o/p in capitalize center:- ",instring1.capitalize().center(20,"*"),end="\n")

searchstring=input("enter a string for search:- ")
print("\n\n")
endposion=int(len(instring1))
print("The o/p in count of string:- ",instring1.count(searchstring,0,endposion),end="\n\n")

print("The encode string is:- ",instring1.encode("ascii","replace"))
import base64
print("The encode string is:- ",base64.b64encode(instring1.encode("utf-8",errors="strict")),end="\n\n")

endstring=input("enter the string to search in end of string:- ")
print("the status of the string",endstring,"at end is:- ",instring1.endswith(endstring,0,endposion))

startstring=input("enter the string to search in start of string:- ")
print("the status of the string",startstring,"at end is:- ",instring1.startswith(startstring,0,endposion))

#expandtabs
mystring="a\tl\to\tk"
print("the expandtab of the string is \n",mystring.expandtabs()) #by default it space is 8 char 

print("the expandtab of the string is \n",mystring.expandtabs(2))

tabcount=int(input("the tab count for a string:- "))

print("\nthe expandtab of the string is \n",mystring.expandtabs(tabcount))

#find it's o/p is(-ve) if result is not found
findstring=input("enter the string to find the position:- ")
print("the position string",findstring,"present on string",instring1,"in position is",instring1.find(findstring,0,endposion))

#casefold (it convert string to small letter)
print("the case fold is ",instring1.casefold())

#compare of 2 string by casefold
instring3=input("enter 1ststring to compare")
instring4=input("enter 2ndstring to compare")
if (instring3.casefold()==instring4.casefold()):
	print("the 2 string is same")
else:
	print("the string is not same")

# index it give error if result not found

print("the position string",findstring,"present on string",instring1,"in position is",instring1.index(findstring,0))


#isalnum
if instring1.isalnum()== True:
	print("the string contain alphabet and numaric number")
else:
	print("the string contain alphabet with space and spacial character")






