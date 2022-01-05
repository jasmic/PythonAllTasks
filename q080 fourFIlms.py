#python programming tasks q080

array = []
for i in range (0,4):
    film = input("please enter the name of a film")
    array.append(film)
print(array[0:2])
array.remove(array[-1])
print(array)
print(array[0:1])
