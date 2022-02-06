#PythonAllTasks q97

file = open("test3.txt","w")
print("Please enter the names of your three favourite songs")
for x in range (3):
    song = input("Enter the name of a song")
    file.write(song)
file.close()

#song1 = input("Please enter the name of your favourite song\n")
#file.write(song1)
#song2 = input("What is the name of your next most favourite song?\n")
#file.write(song2)
#song3 = input("And what is the name of your next most favourite song?")
#file.write(song3)
#file.close()

fileRead = open("test3.txt","r")
read = fileRead.read()
fileRead.close()
print(read.lower())





