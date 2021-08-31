"""
Run Dice Application
	Program Info
		Elisha Victor
		CSC 119 - 005
		Run Dice Application
		11/27/2018
		Run Dice sequence to seperate duplicates
		Version: Uno
"""
import math
from random import randint

def RollDice(): #function to roll 20 dice
    dieNumberList = [] #creates a list to store the dice rolls
    die = 0 #sets up the dice
    for index in range(0,21): #defines 20 rolls
        die = randint(1, 6) #makes the rolls 1-6
        dieNumberList.append(die)#adds the rolls to the list
    return dieNumberList#returns a list of rolled dice


def main(): # definition of main program
    #Data to solve problem
    #Variables

    #Constants
    myNumbers = RollDice()#set up a list of dice rolls with the dice roll fucntion
    inRun = False# check if on a run
    spam = False#check if you are spamming parans while on the run
    #Design Solution

    for index in range(0, len(myNumbers)):#setup loop to read through our list of dice rolls
        
        if inRun == True: #define what to do when a run begins
            if not myNumbers[index] == myNumbers[index + 1]:#ends the run if there was one
                print ("", end='')#prints the closing parens to end run
                inRun = False #sets flag to false so that pc knows run ended

                
        if inRun == False: #if not in a run prepare to see if one is coming
            if myNumbers[index] == myNumbers[index + 1]:#checkj if the next number will be a consecutive value
                inRun = True #if so we are on a run
                spam = True #turn the spammer on so that another paren can be added
                print("(", end='') #print the starting run paren

        print(myNumbers[index],end='',)#print the list of numbers through each interation
        if inRun == False and spam == True: #if the run ended and youre able to spam a paren, 
            print(")", end='')#print closing paren and
            spam = False#set spam to false so that end paren is posting when run ended
    #Input

    #Process

    
      
  
    #Output
    
main() # execution of main program
