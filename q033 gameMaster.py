#Python all tasks Q33.

pc=input("Do you play games on a PC?")
console=input("Do you play games on a games console?")

if pc=="yes" and console=="yes":
    print("Games master!")

elif pc=="yes" and console=="no":
    print("PC master!")

elif pc=="no" and console=="yes":
    print("Console master!")

elif pc=="no" and console=="no":
    print("Boring!")

else:
    print("Error")


