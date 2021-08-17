import Hangman
import FourInARow

print("Welcome to My Childhood Games:\n")
choose_game = int(input("Which game whould you like to play today?\n1 - Hangman\n2 - 4 connect\n"))
while choose_game != 1 and choose_game != 2:
    print("Invalid number, please try again\n")
    choose_game = int(input("Which game whould you like to play today?\n1 - Hangman\n2 - 4 connect\n"))

if choose_game == 1:
    Hangman.play_hangman()
if choose_game == 2:
    FourInARow.play_4connect()
