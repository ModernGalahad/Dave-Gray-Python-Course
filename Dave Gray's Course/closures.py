#Closure is a function having access  to the scope of its parent function
#after the parent function has returned.


def parent_function(person):
    coins = 5
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) +  " coins left. ")
        else:
            print( "\n" + person + "is out of coins.")

    return play_game


legolas = parent_function("Legolas")
thranduil = parent_function("Thranduil")

legolas()
legolas()
thranduil()
legolas()
legolas()