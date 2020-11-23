#! python3



"""
from itertools import product
coutdata=[]
cindata=input("please input the data to generate permutations : - ")
cinrepeat=int(input("enter the criteria for repeating value :-  "))
for indexno in product(list(cindata),repeat=cinrepeat):
	coutdata.append(indexno)
print(coutdata)
"""
"""
from itertools import product

def permutation(fundata,funvalue):
	for indexvalue in product(list(fundata),repeat=funvalue):

		finaldata.append(indexvalue)
	return finaldata

finaldata=[]

def printfun(outfresult):
	print("the op is ",list(outfresult))

inputdata=input("enter the data to generate the parmutation :- ")
inputrepvalue=int(input("enter the value cretaria for repetation value : - "))
permutation(inputdata,inputrepvalue)
printfun(finaldata)
"""
"""
import itertools
invalue=int(input("please entter the no of element to be consider for permutation "))
coinfacevalue=['H','T']
finalprobability=[]
 
for indexval in itertools.product(coinfacevalue,repeat=invalue):
	finalprobability.append(indexval)
print(finalprobability)
"""
"""
import itertools
print("the permutation of H and T of a coin is")
inputvalue=int(input("enter the no of combination  for single trail :- "))
coinfacevalue=['H','T']
finalsamplespace=[]

def permutation(indata,invalue):
	for indexvalue in itertools.product(indata,repeat=invalue):
		finalsamplespace.append(indexvalue)
	return finalsamplespace

permutation(coinfacevalue,inputvalue)
print(finalsamplespace)
"""
from itertools import product
from os import system
system("cls")
print("the permutation of the daice is")
inputvalue=int(input("enter the no of combination  for single trail :- "))
daiceface=[1,2,3,4,5,6]
finalsamplespace=[]

def permutation(indata,invalue):
	for indexvalue in product(indata,repeat=invalue):
		finalsamplespace.append(indexvalue)
	return finalsamplespace

permutation(daiceface,inputvalue)

#print("the no of combination for the daice \n",finalsamplespace)
print("\texp_no\t\tdata")
print("\t-------\t\t--------")
for indexno,dataforfinal in list(enumerate(finalsamplespace)):
	print("\t",indexno+1,"\t\t",dataforfinal)























































































