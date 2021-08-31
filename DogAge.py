"""
DogAge
	Program Info
		Elisha Victor
		CSC 119 - 005
		Program Name
		08/27/2018
		Description: Gives the age of a dog in humans, to calculate the dogs age in dog years
		Version Uno
"""


def main(): # definition of the main program
    # Data to solve problem
    # Variables
    humanYears = 0
    dogYears = 0
    # Constants
    DOGYEAR_MULTIPLIER = 7
    #  Design Solution
    #  Input
    welcomeMessage = ("Welcome to the Dog Age Calculator")
    print(welcomeMessage)
    dogNameMessage = ("What is your dogs name? ")
    dogName = (input(dogNameMessage))
    messageOne = "Enter current age of" + " " + dogName + ":"
    print(messageOne)
    humanYears = float(input("Age: "))
    #  Process
    dogYears = humanYears * DOGYEAR_MULTIPLIER
    #  Output
    messageTwo = (dogName + " " + "in dog years is: ")
    print(messageTwo,  dogYears)
    main()
main() # execution of main program
 

