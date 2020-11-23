#! python3
"""
from os import system
from random import choice
from itertools import product,repeat,permutations

system("cls")
inputelement=list(input("please insert the element to be consider for permutation: "))
no_of_trail=int(input("please enter the number of element to be consider for permutation "))
#no_of_exp=int(input("please enter the number of experiment to conduct "))

#print(choice([permutationelement for permutationelement in product(inputelement,repeat=no_of_trail)]))

permutationelement=[]
for indexval in permutations(inputelement,no_of_trail):
	permutationelement.append(indexval)
#for indexval in range(no_of_exp):
#	print(choice(permutationelement))

print(permutationelement)
"""
"""
from os import system
from random import choice
from itertools import product,repeat,permutations

system("cls")
inputelement=input("please insert the element to be consider for permutation: ")
no_of_trail=int(input("please enter the number of element to be consider for permutation "))
permutationelement=[]


permutationelement=permutations(inputelement,no_of_trail)
print(list(permutationelement))
"""
from os import system
from random import choice
from itertools import product,repeat,permutations

system("cls")
list1=['apple','mango','banana','papaya','kaju','onion']

permutation_fruits=permutations(list1)
print(list(permutation_fruits))
