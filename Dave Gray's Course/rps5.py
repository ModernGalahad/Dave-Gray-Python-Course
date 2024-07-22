import sys
import random
from enum import Enum

#rock (dunedain 1) beats scissors (dwarf 3) and paper (elf 2) beats rock
# actually I think I'll use this variant instead, seems more interesting. 
#Bear mauls Ninja
#Ninja beats Hunter
#Hunter shoots Bear 

def master_function():

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_RPS():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            BEAR = 1 #it is tradition (according to Dave) to capitalize the names of constant variables (variables that don't change)
            NINJA = 2
            HUNTER = 3

        print("\n")
        header = " 🏁 "
        full_header = header.center(23, "=")
        print(full_header)

        player_choice = input("Enter:\n1 for Bear, \n2 for Ninja, or \n3 for Hunter \n\n")
        int_player_choice = int(player_choice)

        if player_choice not in ["1", '2', '3']:
            print("Invalid answer, please input 1,2, or 3.")
            return play_RPS()

        
        else:
            computer_choice = random.choice("123")
            int_computer_choice = int(computer_choice)

        print(" ")
        print("You chose " + str(RPS(int_player_choice)).replace('RPS.', '') + ".")
        print("Python chose " + str(RPS(int_computer_choice)).replace('RPS.', '') + ".")
        print(" ")
        def decide_winner(int_playerchoice, int_computer_choice):
            nonlocal player_wins
            nonlocal python_wins
            if int_player_choice == 3 and int_computer_choice == 1:
                player_wins += 1
                return"🎉 You win!"
            elif int_player_choice == 1 and int_computer_choice == 2:
                player_wins += 1
                return"🎉 You win!"
            elif int_player_choice == 2 and int_computer_choice == 3:
                player_wins += 1
                return"🎉 You win!"
            elif int_player_choice == int_computer_choice:
                return"😮 It's a tie!"
            else:
                python_wins += 1
                return"🐍 Python wins!"
        
        game_result = decide_winner(int_player_choice, int_computer_choice)

        print(game_result)
        nonlocal game_count
        game_count += 1

        print("\nGame Count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

        print("\n Play again?")
        while True:
            playagain = input("(y/n)\n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            play_RPS()
        elif playagain.lower() == "n":
            play_again = False
            print("\nThank you for playing!")
            sys.exit("Goodbye!" + "\n" + "=" * 23)
    return play_RPS
            
game_count = 0

play = master_function()
play()