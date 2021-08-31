"""
    Card Calculator
    Program Info
    Elisha Victor
    CSC 119 - 005
    Card Calculator
    10/17/18
    Tells you what card you have based on the Value and the Suit
    Version: Uno
"""
def main(): # definition of the main program
    # Data to solve problem
    suitValue = ""
    cardValue = 0
    cardNotaion = ""
    exitFlag = False
    errorFlag = False
    # Design Solution
    # Input / data coming in to program
    
    
    # Process
    #Program Loop
    while exitFlag == False:
        cardNotaion = input("Enter the Card Notaion(Value, Card Suit): ",)
        if cardNotaion[1] != "0" or cardNotaion[1] != "D" or cardNotaion[1] != "H" or cardNotaion[1] != "S" or cardNotaion[1] != "C":
                errorFlag = True
        #First Char in Card Notation (Value)
        if cardNotaion[0] == "A":
            cardValue = "Ace"
            errorFlag = False
        elif cardNotaion[0] == "Q":
            cardValue = "Queen"
            errorFlag = False
        elif cardNotaion[0] == "J":
            cardValue = "Jack"
            errorFlag = False
        elif cardNotaion[0] == "K":
            cardValue = "King"
            errorFlag = False
        #switch statement for numbers would be cleaner?
        elif cardNotaion[0] == "2":
            cardValue = 2
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "3":
            cardValue = 3
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "4":
            cardValue = 4
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "5":
            cardValue = 5
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "6":
            cardValue = 6
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "7":
            cardValue = 7
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "8":
            cardValue = 8
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "9":
            cardValue = 9
            cardValue = int(cardValue)
            errorFlag = False
        elif cardNotaion[0] == "1" and cardNotaion[1] == "0" :
            cardValue = 10
            cardValue = int(cardValue)
            errorFlag = False
        else:
            errorFlag = True
        
        #Second Char in Card Notation (Card Suit)
        #Two Length
        if len(cardNotaion) == 2:
            if cardNotaion[1] == "D":
                suitValue = "Diamonds"
                errorFlag = False
            elif cardNotaion[1] == "H":
                suitValue = "Hearts"
                errorFlag = False
            elif cardNotaion[1] == "S" :
                suitValue = "Spades"
                errorFlag = False
            elif cardNotaion[1] == "C":
                suitValue = "Clubs"
                errorFlag = False
            else:
                errorFlag = True
        #Three Length
        elif len(cardNotaion) == 3:
            if cardNotaion[2] == "D":
                suitValue = "Diamonds"
                errorFlag = False
            elif cardNotaion[2] == "H":
                suitValue = "Hearts"
                errorFlag = False
            elif cardNotaion[2] == "S":
                suitValue = "Spades"
                errorFlag = False
            elif cardNotaion[2] == "C":
                suitValue = "Clubs"
                errorFlag = False
            else:
                errorFlag = True
        
        #exit loop
        if cardNotaion == "":
            exitFlag = True
        # Output / answer to problem
        if errorFlag == False:
            print("Your card is the :", cardValue, " of ", suitValue, "\n Press Enter to Quit")
        elif errorFlag == True:
            print("Invalid Input")
        

main() # execution of main program
