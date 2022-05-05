#OOP Assignment

#create a class
class Character: 
    #Initilaize constructor
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    #Initialzie a speak method
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.name + " " + self.phrase1)
        elif phraseNum == 2:
            print(self.name + " " + self.phrase2)

    #Initialize a level method
    def setLevel(self, newLevel):
        self.level = newLevel
        print("Level of " + str(self.level))


#create characters 
character1 = Character("Bingo", "Me and my monkey", "Monkey has no pants")
character2 = Character("Tyrone", "My place", "The chicken was dry")


#character actions
character1.speak(1)
character1.speak(2)
character1.setLevel(2)

character2.speak(1)
character2.speak(2)
character2.setLevel(2)