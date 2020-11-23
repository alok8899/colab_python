#! python3
"""
from os import system
from random import choice
from itertools import product,repeat

system("cls")
daicefacevalue=['H','T']
no_of_trail=int(input("please enter the number of element to be consider for permutation "))
no_of_exp=int(input("please enter the number of experiment to conduct "))

#print(choice([permutationelement for permutationelement in product(daicefacevalue,repeat=no_of_trail)]))

permutationelement=[]
for indexval in product(daicefacevalue,repeat=no_of_trail):
	permutationelement.append(indexval)
for indexval in range(no_of_exp):
	print(choice(permutationelement))
"""
"""
from os import system
from random import choice
from itertools import product,repeat

system("cls")
daicefacevalue=[1,2,3,4,5,6]
no_of_trail=int(input("please enter the number of element to be consider for permutation "))
no_of_exp=int(input("please enter the number of experiment to conduct "))

#print(choice([permutationelement for permutationelement in product(daicefacevalue,repeat=no_of_trail)]))

permutationelement=[]
for indexval in product(daicefacevalue,repeat=no_of_trail):
	permutationelement.append(indexval)
for indexval in range(no_of_exp):
	print(choice(permutationelement))
"""
"""
from os import system
from random import choice
from itertools import product,repeat

system("cls")

list1=[(1,-1),(2,-2),(3,-3)]

pemutationlist=list(product(*list1,repeat=len(list1)))
print(choice(pemutationlist))
"""
"""
from os import system
from random import choice
from itertools import product,repeat

system("cls")

list1=['apple','banana','papaya','guava','kaju','badam','capsicorn']
no_of_trail=int(input("please enter the number of element to be consider for permutation "))

pemutationlist=list(product(list1,repeat=no_of_trail))
print(pemutationlist)
print(len(pemutationlist))
print(len(list1))
print(choice(pemutationlist))
"""
"""
from os import system
from random import choice
from itertools import product,repeat

system("cls")

resurch_metal_list=['pb','mg','h','fc','na','cl','ag']
no_of_trail=int(input("please enter the number of element to be consider for permutation "))

pemutationlist=list(product(resurch_metal_list,repeat=no_of_trail))
print(pemutationlist)
print(len(pemutationlist))
print(len(resurch_metal_list))
print(choice(pemutationlist))
"""


































































































