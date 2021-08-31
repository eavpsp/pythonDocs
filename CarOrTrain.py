"""
Route Calculator
	Program Info
		Elisha Victor
		CSC 119 - 005
		Route Calculator
		08/29/2018
		Calculates the cost of driving versus  the cost of using the train
		Version: Uno
"""
def main(): #definition of main program
    #Data to solve problem
    #Variables
    distanceToJob = 0
    carMPG = 0
    trainTicket = 0
    costToDrive = 0
    #Constants
    GAS_PER_GALLON = 2.7
    DMG_PER_MILE = 0.05
    #Design Solution
    #Input
    distanceToJob = float(input("How far is your Job in miles? "))
    carMPG = float(input("What is your Car's MPG? "))
    trainTicket = float(input("How much is the train ticket? "))
    #Process
    costToDrive = (distanceToJob / carMPG) * GAS_PER_GALLON + (distanceToJob * DMG_PER_MILE)
    #Output 
    print("The cost of a train ticket is ", "$", "%.2f" % trainTicket)
    print("The cost to drive is ","$","%.2f" % costToDrive)
    if costToDrive < trainTicket :
        print("It is cheaper to Drive!")
    else :
        print("It is Cheaper to take the Train!")
    main()
main() # execution of main program
