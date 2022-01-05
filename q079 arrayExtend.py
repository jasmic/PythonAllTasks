#python programming tasks q079

array = []
for i in range (0,3):
    game = input("please enter the name of a game")
    array.append(game)
array.sort()
number=int(input("Which game would you like to see, 1, 2 or 3?"))
print(array[number-1])

