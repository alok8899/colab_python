#! python3



import os
os.system("cls")
flo=sle=tlh=tls=mta=mtg=scp=scl=ssg=ssh=0


def sinput():
	stuname=input("Enter the student name: ")
	flo=float(input("Enter the fast language mark: "))
	sle=float(input("Enter the second language mark: "))
	tlh=input("Enter the third language (hindi)mark: ")
	tls=input("Enter the third language (sanscrit)mark: ")
	mta=float(input("Enter the math paper 1 mark: "))
	mtg=float(input("Enter the math paper 2 mark: "))
	scp=float(input("Enter the science paper 1 mark: "))
	scl=float(input("Enter the science paper 2 mark: "))
	ssg=float(input("Enter the geography  mark: "))
	ssh=float(input("Enter the history mark: "))
	total(stuname,flo,sle,tlh,tls,mta,mtg,scp,scl,ssg,ssh)
	return 



def total(stuname,flo,sle,tlh,tls,mta,mtg,scp,scl,ssg,ssh):
	stotalmark=flo+sle+tlh+tls+mta+mtg+scp+scl+ssg+ssh
	percentage=(totalmark/1000.00)*100
	print("the total mark for",stuname,"is",stotalmark)
	return

myexit=True
while myexit==True:
	os.system("cls")
	sinput()
	total(stuname,flo,sle,tlh,tls,mta,mtg,scp,scl,ssg,ssh)
	responce=input("do you want to enter another student data(Y or N)")
	if responce=="n" or responce=="N":
		myexit=False

#plz short out the problem






