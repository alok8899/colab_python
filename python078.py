#! python3

import os
os.system("cls")

"""
myfilehandle=open("D://python_test_file//test001.txt",mode='a',encoding='cp1252')

writedata=input("\n please enter any text ")

myfilehandle.write(writedata + "\n")
print("the data are write sucessfully")

myfilehandle.close()

"""
"""
myfilehandle=open("D://python_test_file//test001.txt",mode='r',encoding='cp1252')

readdata=myfilehandle.read()

myfilehandle.close()

print(readdata)
"""
"""
myfilehandle=open("D://python_test_file//test002.txt",mode='a',encoding='cp1252')

writedata1=input("\n please enter any text ")
writedata2=input("\n please enter any text ")
writedata3=input("\n please enter any text ")
writedata4=input("\n please enter any text ")

myfilehandle.write(writedata1 + "\n"+writedata2 + "\n"+writedata3 + "\n"+writedata4 + "\n")
print("the data are write sucessfully")

myfilehandle.close()

myfilehandle=open("D://python_test_file//test002.txt",mode='r',encoding='cp1252')
readdata=myfilehandle.read(-1)

print("\nthe data after reading data......")
print(readdata)

myfilehandle.close()
"""
"""
myfilehandle=open("D://python_test_file//test002.txt",mode='a',encoding='cp1252')

writedata1=input("\n please enter any text ")
writedata2=input("\n please enter any text ")
writedata3=input("\n please enter any text ")
writedata4=input("\n please enter any text ")

myfilehandle.write(writedata1 + "\n"+writedata2 + "\n"+writedata3 + "\n"+writedata4 + "\n")
print("the data are write sucessfully")

myfilehandle.close()

myfilehandle=open("D://python_test_file//test002.txt",mode='r',encoding='cp1252')
readdata=myfilehandle.readline(7)

print("\nthe data after reading data......")
print(readdata)

myfilehandle.close()
"""
import itertools
print("\n",dir(itertools),end="\n")















