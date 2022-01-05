#Python all tasks Q22.

name=input("What is your name?") #Asks the user how they are feeling​
print("Hello,", name)
mood=input("How are you feeling today?")

if mood=="happy":
    print("Glad to hear it.")     # This is the response for "happy"
elif mood=="sad":
    print("What do you call a fly with no wings?")
    answer=input()
    print("A walk!")              # This is the response for "sad"
else:
    print("I am sorry, I do not understand.")
                                  # This is the error response
