import sys
import random
from enum import Enum

#rock (dunedain 1) beats scissors (dwarf 3) and paper (elf 2) beats rock
# actually I think I'll use this variant instead, seems more interesting. 
#Bear mauls Ninja
#Ninja beats Hunter
#Hunter shoots Bear 

class RPS(Enum):
    BEAR = 1 #it is tradition (according to Dave) to capitalize the names of constant variables (variables that don't change)
    NINJA = 2
    HUNTER = 3

play_again = True

while play_again:
    print("\n")

    player_choice = input("Enter:\n1 for Bear, \n2 for Ninja, or \n3 for Hunter \n\n")
    int_player_choice = int(player_choice)
 
    if int_player_choice < 1 or int_player_choice > 3:
        sys.exit("Invalid answer, please input 1,2, or 3.")
    
    else:
        computer_choice = random.choice("123")
        int_computer_choice = int(computer_choice)

    print(" ")
    print("You chose " + str(RPS(int_player_choice)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(int_computer_choice)).replace('RPS.', '') + ".")
    print(" ")

    if int_player_choice == 3 and int_computer_choice == 1:
        print("🎉 You win!")
    elif int_player_choice == 1 and int_computer_choice == 2:
        print("🎉 You win!")
    elif int_player_choice == 2 and int_computer_choice == 3:
        print("🎉 You win!")
    elif int_player_choice == int_computer_choice:
        print("😮 It's a tie!")
    else:
        print("🐍 Python wins!")
    
    playagain = input("Do you want to play again? (y/n)\n")
    if playagain.lower() == y:
        





