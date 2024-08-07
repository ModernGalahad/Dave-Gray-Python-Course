import random
import sys


def roll():
    roll = random.randint(1,6)
    print(roll)

    return roll



pl = input("\nHow many players will be playing? At least 2 players and at most 4 are required to start the game. \n")
nrplayers = int(pl)

if nrplayers > 4 or nrplayers < 2:
    sys.exit("Invalid answer. Please try again.")

playerscores = [0 for _ in range(nrplayers)]
max_score = 50

while max(playerscores) < max_score:
    
    for playeridx in range(nrplayers):
        print("\n Player",playeridx + 1, " turn has just started.")
        while True: 
            current_score = 0

            should_roll = input("Would you like to roll (y)?")
            if should_roll.lowercase != "y":
                break
            roll_value = roll()

            if roll_value == 1:
                print("Oh no. You got a 1 and lost your score...")
                break
            else:
                current_score += roll_value
                print("Your rolled a: ", roll_value)

            print("Your score is: ", current_score)
        playerscores[playeridx] += current_score    
        print("Your total score: ", playerscores[playeridx])





