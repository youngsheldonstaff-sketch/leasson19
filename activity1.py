import random

playing = True

num = str(random.randint(10,20))


print("i will generate a random number beetween 10 and 20")
print("the game will end when you get one right")

while playing:
    guess = input("what is your guess?")
    if guess ==num:
        print("you win the game!")
        print("the number was ",num)
        break
    else:
        print("wrong answer, try again!",num)