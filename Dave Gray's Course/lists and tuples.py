users = ['Elrond', 'Gandalf', 'Thorin', 'Bilbo']

data = ['Elrond', 556, True]
emptylist = []

# print('Dave' in emptylist)

# print(users[0])
# print(users[-3])

# print(users.index('Elrond'))
# print(users[0:2])
# print(users[1:])

# print(len(users))

users.append('Galadriel')
#users += 'Melkor'
users += ['Legolas']
print(users)

users.extend(['Bifur','Bombur'])
# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)
users[2:5] = ['Iluvatar','Sauron'] #this replaces objects at the current index
print(users)

users.remove('Sauron')
print(users)

print(users.pop(1)) #removes the value from the list and prints it

del users[0]
print(users)

#del data
data.clear()
print(data)

users[1:2] = ["grond"]
users.sort()
print(users)

users.sort(key=str.lower) #sorts in an alphabetical order even though an object of the list is lowercase
print(users)
del users
del data
#when sorting, make sure you have the SAME type of data
nums = [12,1,2,3,4,5]
# nums.reverse()
# print(nums)

# nums.sort(reverse = True)
# print(nums)

print(sorted(nums,reverse=True)) # does not modify the original list
print(nums)

numscopy = nums.copy()
mycopy = list(nums)
mycopy2 = nums[:] 

#all of the above are copies of the origianl nums list

#Tuples - very similar to lists, data inside and the order can't be changed.

mytuple = tuple(('Elrond', 335, False))
tuple2 = (1, 5, 3, 5, 3, 3)
print(type(mytuple))
print(type(tuple2))

#Adding a value to a tuple (can only be done by creating a new copy of latter tuple) This is called "packing" the tuple.
newlist = list(mytuple)
newlist.append('Grond')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *sike) = tuple2 # the * assigns to that variable all the other remaining objects in the tuple
print(one)
print(two)
print(sike)

print(tuple2.count(3)) # counts the number of the same objects in a tuple