#Python all tasks Q15

#Ask how many apples the user wants.
#Ask how many people the user will share the apples with.
#Find out how many apples will remain if you share the apples equally.
#Hint: use modulus %.

apples=int(input("How many apples do you want?"))
people=int(input("How many people will you share the apples with?"))
remain=apples%people
print(remain)
