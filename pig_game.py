import random
import sys


def roll():
    roll = random.randint(1,6)
    print(roll)

    return roll



players = input("\nEnter the number of players (2-4):\n")
nrplayers = int(players)

if nrplayers > 4 or nrplayers < 2:
    sys.exit("Invalid answer. Please try again.")

playerscores = [0 for _ in range(nrplayers)]
max_score = 50

while max(playerscores) < max_score:
    
    for playeridx in range(nrplayers):
        print("\n" + "=".center(24,"="))
        print("Player",playeridx + 1, "\'s turn has just started.")
        print("Your total score is:", playerscores[playeridx], "\n")

        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            roll_value = roll()

            if roll_value == 1:
                print("\nOh no. You got a 1 and lost your score. Turn done!")
                current_score = 0
                break
            else:
                current_score += roll_value
                print("Your rolled a: ", roll_value)

            print("Your score is:", current_score)

            playerscores[playeridx] += current_score    
            print("Your total score:", playerscores[playeridx])


max_score = max(playerscores)
winning_idx = playerscores.index(max_score)
print("\n Player number", winning_idx + 1, "won with a score of", max_score)



