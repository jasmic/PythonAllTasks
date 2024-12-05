#python programming tasks q077

##number = []
##for i in range (0,5):
##    number.append(int(input("Please enter a number")))
##    number.sort()
##number.reverse()
##print(number)

array = []
for i in range (0,5):
    number = int(input("please enter a number"))
    array.append(number)
array.reverse()
print(array)

# Added 05.12.2024
# Showing how the number input can be added to the array append in a single line
# #Q77
array=[]
for i in range(0,5):
    array.append(input("Enter a number. "))
array.reverse()
print(array)
