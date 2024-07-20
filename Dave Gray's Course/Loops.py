import random
value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1 
# while value <= 10:
#     value += 1 
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Finished. Value is now equal to " + str(value))

names = ["Elrond", "Melkor", "Mithrandir"]
# for x in names:
#     print(x)

# for x in "Random thing": 
#     print(x)

# for x in names:
#     if x == "Melkor"
#         break
#     print(x)


# for x in names:
#     if x == "Melkor":
#         continue
#     print(x)

# for x in range(6):
#     print(x)


# for x in range(1,4):
#     print(x)

for x in range(0,100, 5): # this makes it count by 5 instead of 1
    print(x)
else:
    print("Glad that is over...(joking I'm not XD)")


names = ["Elrond", "Melkor", "Mithrandir"]
actions = ["deciphers", "kills", "travels"]

# for name in names:
#     for action in actions:
#         print(name + " " + random.choice(actions) + ".") # spiced it up a bit :D

for action in actions:
    for name in names:
        print(name + " " + action + ".")