#PythonAllTasks
#print name x times

name=input("What is your name")
num=int(input("Give me a number between 1 and 100"))
if num<=100 and num>0:
    for i in range(num):
        print(name)
        print(i+1)
else:
    print("I asked for a number between 1 and 100!")
