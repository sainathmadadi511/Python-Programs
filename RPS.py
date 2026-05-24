# rock, paper, scissor game.
# want to play ! let's dive in.

computer_choice = "paper";
user_choice = input("Choose rock, paper, or scissor!")

if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissor":
    print("You Win")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win")
elif user_choice == "scissor" and computer_choice == "paper":
    print("You Win")
else:
    print("You Lose and Computer Win!")