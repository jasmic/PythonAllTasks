#Python all tasks Q16

#Asks for the home team name.
#Asks for the opponent team name.
#Asks for the number of goals scored by the home team.
#Asks for the number of goals scored by the opposition team.
#Calculates the goal difference for the home team. 

home=input("What is the name of the Home team?")
away=input("What is the name of the Away team?")

goalsFor=int(input("How many goals did the home team score?"))
goalsAgainst=int(input("How many goals did the Away team score?"))

goalDiff=goalsFor-goalsAgainst
print(goalDiff)
