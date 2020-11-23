#! python3



import os
os.system("cls")
flo=sle=tlh=tls=mta=mtg=scp=scl=ssg=ssh=0

myexit=True
while myexit==True:
	os.system("cls")
	stuname=input("Enter the student name: ")
	flo=float(input("Enter the fast language mark: "))
	sle=float(input("Enter the second language mark: "))
	optional=input("please type optional subject\"H\" for hindi and \"S\" for sanscrit")
	if  optional=="h" or optional=="H":
		tlh=float(input("Enter the third language (hindi)mark: "))
	elif optional=="s" or optional=="S":
		tls=float(input("Enter the third language (sanscrit)mark: "))
	else:
		print("enter proper data")
	mta=float(input("Enter the math paper 1 mark: "))
	mtg=float(input("Enter the math paper 2 mark: "))
	scp=float(input("Enter the science paper 1 mark: "))
	scl=float(input("Enter the science paper 2 mark: "))
	ssg=float(input("Enter the geography  mark: "))
	ssh=float(input("Enter the history mark: "))

	totalmark=flo+sle+tlh+tls+mta+mtg+scp+scl+ssg+ssh
	percentage=(totalmark/900.00)*100
	print("the total mark for",stuname,"is",totalmark)
	responce=input("do you want to enter another student data(Y or N)")
	if responce=="n" or responce=="N":
		myexit=False








