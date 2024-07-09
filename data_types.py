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
title = "Middle-earth's Armory".upper()
title_with_header = title.center(20, "=")
print(title_with_header)
print(title.center(20, "="))