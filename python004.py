#! python3

import os
os.system("cls")

#val1=int(input("Enter 1ST integer value- "))
#val2=int(input("Enter 2nd integer value- "))

val1=float(input("Enter 1ST float value- "))
val2=float(input("Enter 2nd float value- "))

addision=val1+val2
subtraction=val1-val2
multiplication=val1*val2
modulus=val1%val2
exponent=val1**val2
floordiv=val1//val2

print("The addision of two no is ",addision,end="\n")
print("The subtraction of two no is ",subtraction,end="\n")
print("The multiplication of two no is ",multiplication,end="\n")
print("The modulus of two no is ",modulus,end="\n")
print("The exponent of two no is ",exponent,end="\n")
print("The floordiv of two no is ",floordiv,end="\n")
