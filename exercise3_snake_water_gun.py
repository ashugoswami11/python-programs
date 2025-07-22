import random as rand

from django.utils.translation import trim_whitespace

list = ["snake","water","gun"]
comp_choice = rand.choice(list)

counter = 10
score_computer = 0
score_user = 0

while counter > 0:
    print("chances left are:-- ",counter," out of 10")
    user_input = trim_whitespace(input(f"enter your choices:-- {"snake"},{"water"},{"gun"}\n"))

    if user_input == comp_choice:
        print("it's a tie!")
        score_computer +=1
        score_user +=1

    elif (user_input,comp_choice) in [("snake","water"),("water","snake")]:
        if user_input == "snake":
            print("you won")
            score_user +=1
        else:
            print("computer won")
            score_computer +=1

    elif (user_input,comp_choice) in [("gun","water"),("water","gun")]:
        if user_input == "water":
            print("you won")
            score_user +=1
        else:
            print("computer won")
            score_computer +=1

    elif (user_input,comp_choice) in [("gun","snake"),("snake","gun")]:
        if user_input == "gun":
            print("you won")
            score_user +=1
        else:
            print("computer won")
            score_computer +=1
    else:
        print("wrong input")

    counter = counter-1
    if counter == 0:
        print("\ngame end\n")


if score_computer == score_user:
    print("this game is a tie no one won")
elif score_user > score_computer:
    print("your score is",score_user,
        "computer score is",score_computer)
    print("****you won this game*****")
else:
    print("your score is", score_user,
        "computer score is", score_computer)
    print("****computer won this game*****")
