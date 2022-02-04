#PythonAllTasks q93 5RandomNum

import random
ranNums = []
for x in range (5):
    number = random.randint(1,100)
    print("The random number is",number)
    ranNums.append(number)
ranNums.sort()
print(ranNums)






