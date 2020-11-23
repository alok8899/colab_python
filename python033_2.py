#isdecimal

if ("\u00B2".isdecimal()== True):
	print("the data is decimal ")
else:
	print("the data is not not decimal")



#isdigit
if ("\u00B2".isdigit()== True):
	print("the data is digit ")
else:
	print("the data is not not digit")


#isnumeric
if ("\u00B2".isnumeric()== True):
	print("the data is numaric ")
else:
	print("the data is not not numaric")



#isdecimal

if ("\u00BC".isdecimal()== True):
	print("the data is decimal ")
else:
	print("the data is not not decimal")



#isdigit
if ("\u00BC".isdigit()== True):
	print("the data is digit ")
else:
	print("the data is not not digit")


#isnumeric
if ("\u00BC".isnumeric()== True):
	print("the data is numaric ")
else:
	print("the data is not not numaric")

#print(int("\u00BC"))

#islower
print("the string alok is lower or not:- ","alok".islower())
print("the string aLOK is lower or not:- ","aLOK".islower())

#isupper
print("the string ALOK is upper or not:- ","ALOK".isupper())
print("the string aLOK is upper or not:- ","aLOK".isupper())

#isprintable

print("the string  is printable or not:- ","\n".isprintable())


#isspace
print("the string is spaces or not:- ","alok jj".isspace()) # in between letter space false
print("the string is spaces or not:- "," ".isspace()) #only white space or null

#istitle
print("the string is title alok jj or not:- ","alok jj".istitle())
print("the string is title Alok or not:- ","Alok".istitle())
print("the string is title Alok g or not:- ","Alok g".istitle())


#lower
print("the string is lower alok jj or not:- ","alok jj".lower())
print("the string is lower Alok or not:- ","Alok".lower())
print("the string is lower Alok g or not:- ","Alok g".lower())

#upper
print("the string is upper alok jj or not:- ","alok jj".upper())
print("the string is upper Alok or not:- ","Alok".upper())
print("the string is upper Alok g or not:- ","Alok g".upper())


#swapcase
print("the string is swapcase aLOk jj or not:- ","aLOk jj".swapcase())
print("the string is swapcase alok jj or not:- ","alok jj".swapcase())
print("the string is swapcase ALOK jj or not:- ","ALOK jj".swapcase())
print("the string is swapcase ALOK JJ or not:- ","ALOK JJ".swapcase())

#rjust
print("the string is right adjust aLOk jj or not:- ","aLOk jj".rjust(30,"*"))

#ljust
print("the string is left adjust aLOk jj or not:- ","aLOk jj".ljust(30,"*"))

#lstrip to remove the given character from left
print("the string is left strip          aLOk jj or not:- ","             aLOk jj".lstrip()) # string starts with space 
print("the string is left strip *************aLOk jj or not:- ","**************aLOk jj".lstrip("*"))
print("the string is left strip https\www.alok.behera.gmail.com or not:-" , "https\www.alok.behera.gmail.com".lstrip("https\www."))

#rstrip
print("the string is right strip alok.behera.gmail.com or not:-" , "alok.behera.gmail.com".rstrip(".gmail.com"))

#strip  lead and trailing char
print("the string is both strip      alok        or not:-" , "      alok    ".strip())
print("the string is both strip *********alok******* or not:-" , "********alok********".strip("*"))








