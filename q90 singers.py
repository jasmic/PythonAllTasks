#PythonAllTasks q90 Singers

array = []
for i in range (3):
    singer = input("Enter a singer")
    array.append(singer)
array.sort()
#print(array) temp code to check array was being populated and sort working
for x in range(len(array)):
    print("Singer number",x+1,"is",array[x])





