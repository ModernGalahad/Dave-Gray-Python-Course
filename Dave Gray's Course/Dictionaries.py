# Dictionaries

army = {
    "elves": "Plant",
    "guitar": "Page"
}

army2 = dict(elves = "Plant", guitar = "Page")

print(army)
print(army2)
print(type(army))
print(len(army))

#Access items
print(army["elves"])
print(army.get("guitar"))

#list all keys 
print(army.keys())

#list all values
print(army.values())

#List of key/value pairs as tuples
print(army.items()) #inside this list, each pair is a tuple

#verify if a key exists
print("guitar" in army)
print("triangle" in army)

#change values
army["elves"] = "elrond"
army.update({"orcs": "Azog"})
print(army)

#remove items
print(army.pop("orcs"))
print(army)

army["Dunedains"] = "Aragorn"

print(army.popitem())

#Delete and Clear
army["Dunedains"] = "Aragorn"
del army["Dunedains"]
print(army)

army2.clear()
print(army2)

#Copying dictionaries 
army3 = dict(army) # figured this out myself, without looking at the vid :)
army3 = army.copy()
army3["Orcs"] = "Azog"
print(army3) 

#Nested Dictionaries

regiment1 ={
    "Dunedain":"Aragorn",
    "Elf": "Thranduil"
}
regiment2 ={
    "Orc":"Azog",
    "Wizard": "Mithrandir"
}

main_army ={
    "regiment1": regiment1,
    "regiment2": regiment2,
}

print(main_army)
print(main_army["regiment1"]["Dunedain"])


#Sets

nums = { 1,2,3,4}
nums2 = set((1,2,3,4,5))

print(type(nums))
print(len(nums))

#No duplicates allowed in a set
nums ={1,2,2,3}
print(nums) #python ignores the duplicate

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check if a value exists in a set
print(2 in nums)

#index positions or keys don't work for reference to an element in a set

#Adding a new element to a set
nums.add(8)

#adding elements from one set to another

nums.update(nums2) #can be used with lists, tuples, and dictionaries too
print(nums)

#Merge two sets to create a new one
set_1 = {1,2,3,4}
set_2 = {5,6,7,9}
newset = set_1 | set_2 #I have no idea from where I knew this one lol
newset = set_1.union(set_2)
print(newset)


#Keep only the duplicates
set_1 = {1,2,3,4}
set_2 = {1,5,6}

set_1.intersection_update(set_2)
print(set_1)

#Keep everything except  the duplicates
set_1 = {1,2,3,4}
set_2 = {1,2,6}
set_1.symmetric_difference_update(set_2)
print(set_1)