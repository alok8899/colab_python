#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# decorator


# In[2]:


#! python3
import os
os.system("cls")

def basefunction():           #4
    print("this is the message from base function ")


def callingfunction(callbase): #2
    print("this is the message from calling function")
    return callbase()          #3

print("main module of the application begin here")
print("------------------------------------------")
print("calling to calling function")

callingfunction(basefunction) #1


# In[8]:


# DECORATOR
#! python3

import os
os.system("cls")

def makeupper(instringfun):
    def changeuc():
        extrstring=instringfun()
        return extrstring.upper()
    return changeuc
    

def outmessage():
    return "the letter in capital"

print("main module of application begins here ")
print("calling to function normally\n",outmessage())

print("creating decorator here ")
decoratorfunref=makeupper(outmessage)

print("calling to decorator ")
print(decoratorfunref())


# In[17]:


# PYTHON DECORATOR
#! python3

import os
os.system("cls")

def makeupper(instringfun):
    def changeuc():
        print("hghghg")
        extrstring=instringfun()
        return extrstring.upper()
    return changeuc
    
@makeupper
def outmessage():
    print("ggfg")
    return "the letter in capital"

print("main module of application begins here ")
print("calling to decorator ")
print(outmessage())

