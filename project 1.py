#version 1
import random
print("1.ROCK")
print("2.PAPER")
print("3.SCISSORS")
player1=int(input("choose the number 1-3:"))
if player1==1:
    print("player 1 choose number 1 rock :")
elif player1==2:
    print("player 1 choose number 2 paper :")
elif player1==3:
    print("player 1 choose number 3 scissors :")
player2=random.randint(1,3)
if player2 == 1:
    print("player 2 choose number 1 rock :")
elif player2 == 2:
    print("player 2 choose number 2 paper :")
elif player2 == 3:
    print("player 2 choose number 3 scissors :")

if player1 == player2:
    print("no one win...")
elif player1 ==1 and player2 ==2:
    print("player2 are winner")
elif player1 ==1 and player2 ==3:
    print("player1 are winner")
elif player1 ==2 and player2 ==1:
    print("player1 are winner")
elif player1 ==2 and player2 ==3:
    print("player2 is winner")
elif player1 ==3 and player2 ==1:
    print("player2 are winner")
elif player1 ==3 and player2 ==2:
    print("player1 is winner")

#version 2
import random
from random import randint

print("Rock Paper Scissors Game")

random_num = randint(0, 3)

if random_num == 0:
    Bot = "rock"
elif random_num == 1:
    Bot = "paper"
else:
    Bot = "scissors"
player = input("player : ").lower()

if player == Bot:
    print("Bot: ",Bot)
    print("Tie")
    
elif player == "rock":
    if Bot == "paper":
        print("Bot: ",Bot)
        print("You Lose")
    else:
        print("You Win")
elif player == "scissor":
    if Bot == "rock":
        print("Bot: ",Bot)
        print("You Lose")
    else:
        print("You Win")
elif player == "paper":
    if Bot == "scissors":
        print("Bot: ",Bot)
        print("You win")
    else:
        print("Bot: ",Bot)
        print("You Lose")
else:
    print("you move is not valid")