#python programming tasks q082

males = 0
females = 0
others = 0
storage = []

gender = input("Are you male, female, other or quit?")
storage.append(gender.lower())
while gender.lower() == "male" or gender.lower() == "female" or gender.lower() == "other":
    gender = input("Are you male, female, other or quit?")
    storage.append(gender.lower())
if gender.lower() =="quit":
    for item in storage:
        if item.lower() == "male":
            males = males + 1
        elif item.lower() == "female":
            females = females + 1
        else:
            others = others + 1
    print(str(males) +"males")
    print(str(females) +"females")
    print(str(others) +"others")

#05.01.2022
#I understand what the code is doing but I needed a lot of help writing it!
    




