#PythonAllTasks q94 UserRandomNum

import random
ranNums = []

ranNumNum = int(input("How many random numbers do you want to generate?"))
ranNumRangeLow = int(input("What is the lowest number you want to generate?"))
ranNumRangeHigh = int(input("What is the highest random number you want to generate?"))
       

for x in range (ranNumNum):
    number = random.randint(ranNumRangeLow,ranNumRangeHigh)
    print("The random number is",number)
    ranNums.append(number)
ranNums.sort()
print(ranNums)






