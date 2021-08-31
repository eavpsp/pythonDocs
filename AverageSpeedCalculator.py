"""
AverageSpeedCalculator
	Program Info
		Elisha Victor
		CSC 119 - 005
		AverageSpeedCalculator
		08/29/2018
		Calculates the average speed for a trip to the store
		Version: Uno
"""
def main(): # definition of main program
    #Data to solve problem
    #Variables
    returningSpeed = 0
    timeAtStore = 0
    averageSpeed = 0
    #Constants
    INITIAL_SPEED = 20
    HOUR_TIME = 60
    #Design Solution
    #Input
    timeAtStore = float(input("How many minutes were you at the store? "))
    returningSpeed = float(input("How fast were you driving home? "))
    #Process
    averageSpeed = (INITIAL_SPEED + (timeAtStore/HOUR_TIME) + returningSpeed) / 3
    #Output
    print("Your average speed is: ", "%.2f" % averageSpeed, "MPH")
    main()
main() # execution of main program
