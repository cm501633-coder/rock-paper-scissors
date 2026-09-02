import random
item_list = ["rock", "paper", "scissors"]
user_choice=input("enter your choice rock,paper,sciccors:")
com_choice=random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {com_choice}")
if user_choice==com_choice:
    print("both chooses same:=match tie")
elif user_choice=="rock":
    if com_choice=="paper":
        print("computer wins")
    else:
        print("user wins")
elif user_choice=="paper":
    if com_choice=="scissors":
        print("computer wins")
    else:
        print("user wins")
elif user_choice=="scissors":
    if com_choice=="paper":
        print("user wins")
    else:
        print("computer wins")