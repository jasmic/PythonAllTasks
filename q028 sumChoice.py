#Python all tasks Q29.


num1=int(input("Please enter a number."))
num2=int(input("Please enter another number."))

operator=input("Do you want to add the numbers together, or multiply them?")

if operator=="add":
    answer=num1+num2
    print(answer)
elif operator=="multiply":
    answer=num1*num2
    print(answer)
else:
    print("Sorry, I cannot do that.")


