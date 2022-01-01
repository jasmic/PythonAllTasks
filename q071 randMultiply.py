#PythonAllTasks q72 randMultiply

import random

for i in range(5):
    first = random.randint(1,10)
    second = random.randint(1,10)
    answer = first*second
    guess = int(input(str(first)+" X "+str(second)+" = "))
    if guess == answer:
        print("Correct answer")
    else:
        print("Incorrect answer")
