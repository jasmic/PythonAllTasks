#python programming tasks q087

#Use \ to split up a long line of code

grades = [["Alfie Little",24,32,5],\
          ["Billy Bob Junior II",22,22,53],\
          ["Mark Jones",43,54,23],\
          ["King Plonker",23,12,32]]

print(grades)
grades[0].append(37)
grades[1].append(99)
grades[2].append(32)
grades[3].append(42)
print(grades)

average = (grades[0][1]+grades[0][2]+grades[0][3]+grades[0][4])/4
print("The average for Alfie Little is:",average)







