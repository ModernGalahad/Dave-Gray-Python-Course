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

army["Duendains"] = "Aragorn"

print(army.popitem())