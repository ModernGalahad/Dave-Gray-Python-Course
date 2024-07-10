#String Data Type (literal assignment)
first = "Legolas"
last = "Greenleaf"
# print(type(first))
# print(type(first) == (type)(last)) 
# print(type(first) == str)
# print(isinstance(first,str))

#Constructor Function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza,str))

#Concatenation (this means the joining of strings)
full_name = first + " " + last
full_name += " of Mirkwood"

#Casting a number to a string
decade = str(1130)
#print(type(decade))
#print(decade)

statement = "Born in " + decade + "."
#print(statement)

# Multiple Lines
multiline = '''
It is I, a High Elf, son of Thranduil.                         

I am a skilled archer and warrior.
                                    Who are you?
'''
##print(multiline)

# Escaping Special Character Issues
# "t" is used to add a tab
# "\" is used to make Python ignore special characters like t or n or ' in a string.
# "n" is used to add a new line

sentence = 'I\'m ready to kill some orcs!\tHey\n\nWhere\'s this dwarven friend of yours?' 
#print(sentence)

#String Methods (making strings lowercase or uppercase)
#print(first)
#print(first.lower())
#print(first.upper())

#print(multiline.title())
#print(multiline.replace("warrior","philosopher"))

#print(len(multiline))
multiline += "        "
multiline = "        " +  multiline 
#print(multiline)
#This is a pretty darn cool workaround: first we redefine multiline to be equal to the "   "s 
# and then we concatenate this new value with the original multiline to add the "   "s at the beginning.

#print(len(multiline))

#print(len(multiline.strip()))
#print((multiline.rstrip()))
#print((multiline.lstrip()))
#removes all the whitespace or the whitespace to the left or right of the string

#print(len(multiline))

#Build a menu (in my case, armory)
title = "Middle-earth Armory".upper()
title_with_header = title.center(50, "=")
print(title_with_header)
print("Glamdring".ljust(20, ".")+ "$7".rjust(0))
print("Aeglos".ljust(20, ".")+ "$10".rjust(0))
print("Herugrim".ljust(20, ".")+ "$3".rjust(0))


#String Index Values ---- Indexes start at 0!
print(first[1])
print(first[-1]) #this gives you the last value in a string
print(first[1:-1])
print(first[3:-1])

#Some methods return Boolean data (true or false)
print(first.startswith("L")) or print(first.endswith("D"))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

###Numeric Data Types###

#Integers
price = 100
bestprice = (100)
print(type(price))
print(isinstance(bestprice, int))

#Float Type
gpa = 3.84
y = float(1.14)
print(gpa, y)

#complex value
comp_value = 5+3j
print(type(comp_value)) 
print(comp_value.real)
print(comp_value.imag)

#Built-in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(3.20))
print(math.floor(3.2))

#Casting a string to a number
zipcode = "1100"
zip_value = int(zipcode)
print(type(zip_value))