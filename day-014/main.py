import random
from art import logo , vs
from data import data


def get_alternativa():
    primero , segundo = random.sample(data,2)
    if "country" not in primero:
        primero['country'] = ''
    if "country" not in segundo:
        segundo['country'] = ''
    return primero, segundo



def compare():
    option1 , option2 = get_alternativa()
    print(logo)
    print(f"Compare A: {option1['name']}, {option1['description']}, from {option1['country']}" )
    print(vs)
    print(f"Against B: {option2['name']}, {option2['description']}, from {option2['country']}")

    user_choice = input(f"Who has more followers? Type 'A' or 'B': ")
    if user_choice == 'A':
        if option1['follower_count'] > option2['follower_count']:
            return True
        else:
            return False
    else:
        if option2['follower_count'] > option1['follower_count']:
            return True
        else:
            return False


result = True
score = 0
while result:
    if compare():
        score += 1
        print(f"You win , your score :{score}")
    else:
        print(f"You loose , your score :{score}")
        result = False
