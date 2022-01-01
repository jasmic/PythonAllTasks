#PythonAllTasks q57.

quote = input("Enter a quote")
split = quote.split()
for i in range(len(split)):
    print(split[i][0])
