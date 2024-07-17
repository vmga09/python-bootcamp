import random
from art import logo

print(logo)

def play_game():
    number_choice = random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    nro_lives = 0
    dificult = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if dificult == 'easy':
        nro_lives = 10
    elif dificult == 'hard':
        nro_lives = 4


    result = False
    finish = False
    while nro_lives > 0 and finish == False:
        print(f"You have {nro_lives} attempts remaining to guess the number.")
        intent = int(input("Make a guess: "))
        if intent == number_choice:
            print(f"You got it! The answer was {number_choice}.")
            result = True
            finish = True

        elif intent > number_choice:
            print("Too high.")
            print("Guess again.")
            nro_lives -= 1
        else:
            print("Too low.")
            print("Guess again.")
            nro_lives -= 1
    
    return result


choice = 'yes'
while choice == 'yes':
     if play_game():
         print("You WIN!!!")
     else:
         print(" You lose")
     choice = input("Play again, Type 'yes' or 'no' :")


