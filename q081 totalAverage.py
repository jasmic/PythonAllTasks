#python programming tasks q081

score = []
for i in range (0,6):
    number = int(input("please enter a number"))
    score.append(number)
print(score)

print("Do you want to see the total or average of your numbers?")

option=input("Type total or average")
#total = score[0]+score[1]+score[2]+score[3]+score[4]+score[5]
total=sum(score)
if option == "total":
    print(total)
elif option == "average":
    print(total/6)
else:
    print("invalid option")

