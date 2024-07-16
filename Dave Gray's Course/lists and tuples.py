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

#Tuples 