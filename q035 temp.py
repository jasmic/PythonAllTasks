#Python all tasks Q35.

temp=int(input("Please enter the current temperature."))
rain=input("Is it raining?")

if temp<12 and rain=="yes":
    print("Wear a coat and bring an umbrella.")

elif temp<12 and rain=="no":
    print("Wear a coat.")

elif temp>=12 and rain=="yes":
    print("Bring an umbrella")
    
else:
    print("You do not need a coat or an umbrella. Have a nice day!")


