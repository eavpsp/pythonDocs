"""
MPG Calculator
	Program Info
		Elisha Victor
		CSC 119 - 005
		MPG Calculator
		09/21/2018
		Calculates the cars current Miles Per Gallon based on the miles driven and gas fueled.
		Version: Uno
"""
def main(): # definition of main program
    #Data to solve problem
    #Variables
    milesDriven = 0
    gasToFillTank = 0
    #Constants
    #Design Solution
    #Input
    milesDriven = float(input("How many miles did you drive on this trip? "))
    gasToFillTank = float(input("How many gallons did it take to fill your tank after the trip? "))
    #Process
    milesPerGallon = milesDriven / gasToFillTank
    #Output
    print ("Your MPG is ","%.2f" %  milesPerGallon, "MPG")
    main()
main() # execution of main program
