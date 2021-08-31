"""
Math App
	Program Info
		Elisha Victor
		CSC 119 - 005
		Math App
		09/21/2018
		Calculates the sum, difference, product, average, distance, max and min of the two values inputted by the user.
		Version: Uno
"""
def main(): # definition of main program
    import math
    #Data to solve problem
    #Variables
    firstValue = 0
    secondValue = 0
    sumOfValue = 0
    differenceOfValue = 0
    productOfValue = 0
    averageOfValue = 0
    distanceOfValue = 0
    #Constants
    #Design Solution
    #Input
    firstValue = float(input("Enter the first value: "))
    secondValue = float(input("Enter the second value: "))
    #Process
    sumOfValue = float(firstValue + secondValue)
    differenceOfValue = float(firstValue - secondValue)
    productOfValue = float(firstValue * secondValue)
    distanceOfValue = float(abs(differenceOfValue))
    averageOfValue = float((firstValue + secondValue) / 2)
    maxOfValue = float(max(firstValue, secondValue))
    minOfValue = float(min(firstValue, secondValue))
    #Output
    print ("%-10s %10d" % ("Sum: ", sumOfValue))
    print ("%-10s %9d" % ("Difference:", differenceOfValue))
    print ("%-10s %10d" % ("Product:", productOfValue))
    print ("%-10s %10d" % ("Average:", averageOfValue))
    print ("%-10s %10d" % ("Distance:", distanceOfValue))
    print ("%-10s %10d" % ("Maximum:", maxOfValue))
    print ("%-10s %10d" % ("Minimum:", minOfValue))
    main()
main() # execution of main program
