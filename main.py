#Rock, Paper, Scissors Game
from random import choice

#moves
moves = ["rock", "paper", "scissors"]

while True:
    computer = choice(moves)
    player = input("Choose either rock, paper or scissors (or end the game)--->").lower()
    if player == "end the game":
        print("The game has ended. Hope you enjoyed it")
        break
    elif player == computer:
        print("A draw")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player )
        else:
            print("You win!", player, "beats", computer)
            break
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player )
        else:
            print("You win!", player, "beats", computer)
            break
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player )
        else:
            print("You win!", player, "beats", computer)
            break
    else:
        print("please check your spelling and try again")
