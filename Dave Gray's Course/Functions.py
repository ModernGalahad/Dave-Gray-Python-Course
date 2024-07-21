# def hello():
#     print("Greetings weary traveller!")
# hello()

def sum(number_1=0, number_2=0):
    if (type(number_1) is not int or type(number_2) is not int):
        return 0
    return number_1 + number_2

total = sum()
print(total)

def multiple_things(*args): # used for a yet unkown parameter/s
    print(args)
    print(type(args))

multiple_things("Elrond","Melkor", "Iluvatar")

def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(first = "Mithrandir", last = "The Grey")