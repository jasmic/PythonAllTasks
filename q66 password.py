#PythonAllTasks q66

attempts = 0

while attempts !=4:
    password=input("Please enter a password.")
    attempts = attempts + 1
    if password == "duck":
        print("Correct password")
        attempts = 4
    else:
        print("try again")
print("Locked")

