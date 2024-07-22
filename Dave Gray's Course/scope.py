name = "Elrond"
count = 3
# def  greeting(firstname):
#     color = "red"
#     print(color)
#     print(name)
#     print(firstname)

#     color = "black"

# greeting("John")

def something():
    color = "black" 
    global count
    count += 1 
    print(count)
    
    def  greeting(firstname):
        nonlocal color 
        color = "green"
        print(color)
        print(firstname)
    
    greeting('Dave')
    print(color)

#you can access values from the global scope in the function is possible, but reassinging a value to a variable is not possible.
#This only works when using "global".



something()

#You can also define a function (eg.greeting) inside a function, but that will result in you being able to only call  
#the greeting function inside the function you defined it in because of the local scope.

# try to keep everything in local scope, not global.



