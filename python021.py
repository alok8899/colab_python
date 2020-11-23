#! python3

import os
os.system("cls")

cvalue2000=cvalue500=cvalue200=cvalue100=cvalue50=cvalue20=cvalue10=cvalue5=cvalue2=cvalue1=0

fvalue=invalue=int(input("enter the value :- "))

if (invalue>=2000):
	cvalue2000=int(invalue/2000)
	invalue=invalue-(cvalue2000*2000)

if (invalue>=500):
	cvalue500=int(invalue/500)
	invalue=invalue-(cvalue500*500)

if (invalue>=200):
	cvalue200=int(invalue/200)
	invalue=invalue-(cvalue200*200)

if (invalue>=100):
	cvalue100=int(invalue/100)
	invalue=invalue-(cvalue100*100)

if (invalue>=50):
	cvalue50=int(invalue/50)
	invalue=invalue-(cvalue50*50)

if (invalue>=20):
	cvalue2=int(invalue/20)
	invalue=invalue-(cvalue20*20)

if (invalue>=10):
	cvalue10=int(invalue/10)
	invalue=invalue-(cvalue10*10)

if (invalue>=5):
	cvalue5=int(invalue/5)
	invalue=invalue-(cvalue5*5)

if (invalue>=2):
	cvalue2=int(invalue/2)
	invalue=invalue-(cvalue2*2)

if (invalue>=1):
	cvalue1=int(invalue/1)
	invalue=invalue-(cvalue1*1)

print("\n\n\nthe o/p of no of currency for",fvalue,"is")
print("---------------------------------------------------",end="\n\n\n")


print("the no of dinomination of 2000 for ","%3s"%(":",),fvalue,"is",cvalue2000)

print("the no of dinomination of 500 for ","%4s"%(":",),fvalue,"is",cvalue500)

print("the no of dinomination of 200 for ","%4s"%(":",),fvalue,"is",cvalue200)

print("the no of dinomination of 100 for ","%4s"%(":",),fvalue,"is",cvalue100)

print("the no of dinomination of 50 for ","%5s"%(":",),fvalue,"is",cvalue50)

print("the no of dinomination of 20 for ","%5s"%(":",),fvalue,"is",cvalue20)

print("the no of dinomination of 10 for ","%5s"%(":",),fvalue,"is",cvalue10)

print("the no of dinomination of 5 for ","%6s"%(":",),fvalue,"is",cvalue5)

print("the no of dinomination of 2 for ","%6s"%(":",),fvalue,"is",cvalue2)

print("the no of dinomination of 1 for ","%6s"%(":",),fvalue,"is",cvalue1,end="\n\n\n")

space2000=len(str(sum([cvalue2000,2])))   #think to put on length of space is given in print function
space500=len(str(sum([cvalue500,2])))
space200=len(str(sum([cvalue200,2])))
space100=len(str(sum([cvalue100,2])))
space50=len(str(sum([cvalue50,2])))
space20=len(str(sum([cvalue20,2])))
space10=len(str(sum([cvalue10,2])))
space5=len(str(sum([cvalue5,2])))
space2=len(str(sum([cvalue2,2])))
space1=len(str(sum([cvalue1,2])))


print("The total dinomanations of",fvalue,"is below")
print("----------------------------------------------",end="\n\n")

print("2000*%d%5s=%d"%(cvalue2000,"",(cvalue2000*2000)))
print("500*%d%6s=%d"%(cvalue500,"",(cvalue500*500)))
print("200*%d%6s=%d"%(cvalue200,"",(cvalue200*200)))
print("100*%d%6s=%d"%(cvalue100,"",(cvalue100*100)))
print("50*%d%7s=%d"%(cvalue50,"",(cvalue50*50)))
print("20*%d%7s=%d"%(cvalue20,"",(cvalue20*20)))
print("10*%d%7s=%d"%(cvalue10,"",(cvalue10*10)))
print("5*%d%8s=%d"%(cvalue5,"",(cvalue5*5)))
print("2*%d%8s=%d"%(cvalue2,"",(cvalue2*2)))
print("1*%d%8s=%d"%(cvalue1,"",(cvalue1*1)))


print("TOTAL=%d"%fvalue)


print("2000*",cvalue2000,'{:>4}'.format(':'),(cvalue2000*2000))
print("500*",cvalue500,'{:>6}'.format(':'),(cvalue500*500))
print("200*",cvalue200,'{:>6}'.format(':'),(cvalue200*200))
print("100*",cvalue100,'{:>6}'.format(':'),(cvalue100*100))
print("50*",cvalue50,'{:>7}'.format(':'),(cvalue50*50))
print("20*",cvalue20,'{:>7}'.format(':'),(cvalue20*20))
print("10*",cvalue10,'{:>7}'.format(':'),(cvalue10*10))
print("5*",cvalue5,'{:>8}'.format(':'),(cvalue5*5))
print("2*",cvalue2,'{:>8}'.format(':'),(cvalue2*2))
print("1*",cvalue1,'{:>8}'.format(':'),(cvalue1*1))