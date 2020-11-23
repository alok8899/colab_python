#! python3

from os import system
import random  
from itertools import combinations

system("cls")
naturalnolist=[1,2,3,4,5,6,7,8,9]
print("the original string given for analysis is ",list(naturalnolist))

random.shuffle(naturalnolist)

print("the random shuffle list for amalysis ",list(naturalnolist))
pickupelement=int(input("please enter the number of element to pickup  "))

generatedcombi=combinations(naturalnolist,pickupelement)

print(list(generatedcombi))


































