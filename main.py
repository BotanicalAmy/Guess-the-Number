from art import logo
from random import randint


print(logo)
print("Welcome to the Number Guessing Game!")
number = randint(1, 100)
guess_response = ["Too high.", "Too low.", "You got it!"]
turns = 10
difficulty = input("I'm thinking of a number between 1 and 100.  Choose a difficulty. Type 'easy' or 'hard': ") 
#remove 5 turns for hard
if difficulty == 'hard':
    turns -= 5

def number_compare(player_guess):
    '''Let the player know if their guess was too high, too low, or correct'''
    if player_guess > number:
        return guess_response[0]
    if player_guess < number:
        return guess_response[1]
    if player_guess == number:
        return guess_response[2]

guessing = True
while guessing is True:
    guess = int(input("Make a guess:"))
    turns -= 1
    turns_remaining = str(turns)
    #determine too high, too low, or winner
    print(f"{number_compare(guess)}")
    #end game for correct winner
    if guess == number:
        print(f"The answer was {number}")
        guessing = False
    #end the game if player runs out of turns
    if turns == 0:
        print(f"The answer was {number}")
        guessing = False
    elif guess != number:
        print(f"You have {turns_remaining} attempts remaining.")
    
        


        



