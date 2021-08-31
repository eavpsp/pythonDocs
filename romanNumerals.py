"""
Roman Numerals Application
	Program Info
		Elisha Victor
		CSC 119 - 005
		Roman Numerals Application
		11/27/2018
		Converts Roman Numerals
		Version: Uno
"""
import math
charValue = 0 #defien the value of the numeral
romanNumeral = "" #get the numeral
def convertRomanNumerals(userInput): #function to convert the numeral
        if userInput == "M":  #define each character and assing the value
            charValue = 1000
        elif userInput == "D":
            charValue = 500
        elif userInput == "C":
            charValue = 100
        elif userInput == "L":
            charValue = 50
        elif userInput == "X":
            charValue = 10
        elif userInput == "V":
            charValue = 5
        elif userInput == "I":
            charValue = 1
        else: charValue = 0

        return int (charValue) #return the value of the char
            
            
        
    

def main(): # definition of main program
    #Data to solve problem
    #Variables
    total = 0 #get the total generated from adding the numerals together
    charList = [] #create a list to hold the charaters
    applicationFlag = True #set up application flag to control program loop
    #Constants
    
    #Design Solution
    while applicationFlag == True: #start program loop
        if total > 0:
                total = 0#reset the total each time
        print("Enter a Roman Numeral, Press Enter to quit")#set up prompt for user
        #Input
        romanNumeral = input("")#get the users number to convert
        #Process
        charList = [char for char in romanNumeral] #add the users input to the character list
        if romanNumeral == "": #set up loop break on empty input
            applicationFlag = False#break application loop
        while not len(charList) == 0:#loop to keep tracing back into the list to make sure every char has been read
            if len(charList) > 1: #if there is more than one char in the list
                if convertRomanNumerals(charList[0]) >= convertRomanNumerals(charList[1]): #compare the first value to the second
                    total += convertRomanNumerals(charList[0]) + convertRomanNumerals(charList[1]) #if it is larger or equal to the second value, add them then add it to the total
                    del charList[0:2]#remove the chars from the list so that the program knows to continue
                                                    
                elif convertRomanNumerals(charList[1]) > convertRomanNumerals(charList[0]): #if the first value is less than the second value
                    total += convertRomanNumerals(charList[1]) - convertRomanNumerals(charList[0])#subtract the second value from the first value and add it to the total
                    del charList[0:2]#remove the chars from the list so that the program knows to continue
                    
            elif len(charList) == 1: #if there is only one char
                 total += convertRomanNumerals(charList[0])#add it to the total 
                 del charList[0]#remove the chars from the list so that the program knows to continue
            else:
                break
        print ("The Number Value is: ", total) #print the total to the user
    
      
  
    #Output
    
main() # execution of main program
