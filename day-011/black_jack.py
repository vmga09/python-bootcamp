import random
from art import logo
import os
clear = lambda : os.system("clear")
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def score_card(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,house_score):
    if user_score == house_score:
        return "Draw :) "
    elif house_score == 0:
        return "lose, opponent has Blackjack :o"
    elif user_score == 0:
        return "You Win , yuo have Blackjack :)"
    elif user_score > 21:
        return "You lost "
    elif house_score > 21:
        return "You Win "
    elif user_score > house_score:
        return "You Win"
    else:
        return "You lose"
def play_game():
    print(logo)
    house_card=[]
    user_card=[]
    is_game_over = False

    for _ in range(2):
        house_card.append(deal_card())
        user_card.append(deal_card())
    while  not is_game_over:
        user_score = score_card(user_card)
        house_score = score_card(house_card)

        print(f"Your cards are {user_card}, current score : {user_score}")
        print(f"House first card are {house_card[0]} !!!")

        if user_score == 0 or house_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_option = input(f"Type 'y' for another card,type  'n' to pass: ")
            if user_option == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while house_score != 0 and house_score < 17:
        house_card.append(deal_card())
        house_score = sum(house_card)
    print(f" Your final hand: {user_card} , final score: {user_score}")
    print(f" House final hand: {house_card}, final score :{house_score} ")
    print(compare(user_score,house_score))

while input("Do you o play a game of Blackjack game? Type 'y' or 'n' :") == 'y':
    clear()
    play_game()