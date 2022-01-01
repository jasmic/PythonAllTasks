#PythonAllTasks q68

username = input("Please enter a username")
while len(username)<8:
    username = input("Invalid username, enter another username")
print("Your username has been accepted.")

password = input("Please enter a password")
while len(password)<8 or len(password)>15:
    password = input("invalid password, enter another password")
print("Your password  has been accepted.")
