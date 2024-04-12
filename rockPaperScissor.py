# Rock Paper Scissor Game
import random
player = int(input("Enter\n0 for Rock\n1 for Paper\n2 for Scissors\n->"))
if player == 0:
    print("You-->ROCK")
elif player == 1:
    print("You-->PAPER")
elif player == 2:
    print("You-->SCISSOR")

computer = random.randint(0, 2)
if computer == 0:
    print("Computer-->ROCK")
elif computer == 1:
    print("Computer-->PAPER")
elif computer == 2:
    print("Computer-->SCISSOR")

#  for result
if player == 0 or player == 1 or player == 2:
    if player == computer:
        print("It's a draw.")
    elif player == 0 and computer == 1:
        print("You Lost")
    elif player == 1 and computer == 2:
        print("You Lost")
    elif player == 2 and computer == 0:
        print("You Lost")
    else:
        print("You Won!")
else:
    print("Wrong input from user.")
