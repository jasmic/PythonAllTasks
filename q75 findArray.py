#PythonAllTasks q75 findinarray

array = [2,4,6,8,10]

num = int(input("Enter a number to see if it's in the array"))

for i in range(len(array)):
    if num == array[i]:
        print ("found")

