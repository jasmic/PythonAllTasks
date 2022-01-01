#PythonAllTasks q70 random

import random
ranNum=random.randint(1,100)
guess = int(input("Guess a number between 1 and 100."))

while True:
    if guess > ranNum:
        print("Too high! Try again.")
        guess = int(input("Guess a number between 1 and 100."))
    elif guess < ranNum:
        print("Too low! Try again.")
        guess = int(input("Guess a number between 1 and 100."))
    else:
        print("Well done!")
        break
