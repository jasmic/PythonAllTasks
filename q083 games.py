#python programming tasks q083

games = []



while True:
    menu = input("Do you want to add, edit, delete a game, or print all games?")

    if menu == "add":
        newGame=input("What is the name of the game you want to add?")
        games.append(newGame)
        print("Game "+newGame +" added. ")
    elif menu == "print":
        print("Your games are: ")
        print(games)
    elif menu == "edit":
        print("Your games are: "+str(games))
        editGame=input("Which game do you want to edit?")
        newName=input("What do you want to change it to?")
        games.remove(editGame)
        games.append(newName)
    elif menu == "delete":
        print("Your games are: "+str(games))
        delGame=input("Which game do you want to edit?")
        games.remove(delGame,)
    else:
        print("Invalid option")

