import random

while True:
    inpu = input("enter either: rock,paper,scissors.")
    possibilitys = ["rock","paper","scissors"]
    computer = random.choice(possibilitys)

    print("you chose:",inpu,"while the computer chose:",computer)

    if inpu == computer:
        print("its a tie!")
    elif inpu == "rock":
        if computer == "scissors":
            print("you win!")
        else:
            print("computer wins!")
    elif inpu == "paper":
        if computer == "rock":
            print("you win!")
        else:
            print("computer wins!")
    elif inpu == "scissors":
        if computer == "paper":
            print("you won!")
        else:
            print("computer wins!")

    playagain = input("do you want to play again? y/n: ")
    if playagain != "y":
        break