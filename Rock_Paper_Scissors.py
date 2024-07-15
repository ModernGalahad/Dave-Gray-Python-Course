#value = input('Please enter some classified info:\n')
#print(value)
import sys
import random
print("\n")

player_choice = input("Enter:\n1 for Dunedain, \n2 for Elf, or \n3 for Dwarf \n\n")
int_player_choice = int(player_choice)
 
if int_player_choice < 1 | int_player_choice > 3:
    sys.exit("Invalid answer, please input 1,2, or 3.") 
else:
    computer_choice = random.choice("123")
    int_computer_choice = int(computer_choice)

    print(" ")
    print("You chose " + str(int_player_choice) + ".")
    print("Python chose " + str(int_computer_choice) + ".")
    print(" ")
