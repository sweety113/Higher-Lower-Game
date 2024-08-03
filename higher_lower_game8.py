#search in google
import random
import os
import game_logo
import game_data


print(game_logo.game_Art)
score=0

def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, {description}, from {country}"

def check_answer(guess,follower_1,follower_2):
    if follower_1<follower_2:
        if guess==1:#return guess==2
            return False
        else:
            return True
    else: 
        if guess==1:
            return True
        else:
            return False

account_2=random.choice(game_data.data)

continue_flag=True
while continue_flag:
    account_1=account_2
    account_2=random.choice(game_data.data)

    while account_1==account_2:#same accounts generated if
        account_2=random.choice(game_data.data)

    print(f"compare 1: {display_accountinfo(account_1)}")
    print(game_logo.vs)
    print(f"compare 2: {display_accountinfo(account_2)}")

    guess=int(input("Who has more followers? Type 1 or 2: "))
    follower_count_1=account_1["follower_count"]
    follower_count_2=account_2["follower_count"]
    
    is_correct=check_answer(guess,follower_count_1,follower_count_2)
    os.system('cls')
    print(game_logo.game_Art)
    if is_correct:
        score +=1
        print(f"You are right.Your score is :{score}")
    else:
        print(f"You are wrong.Your final score is :{score}")
        continue_flag=False












































