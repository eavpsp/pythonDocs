"""
Theater Seating Chart
	Program Info
		Elisha Victor
		CSC 119 - 005
		Theater Seating Chart
		11/27/2018
		Get the theaters seating chart and lets the user purchase up to 5 tickets
		Version: Uno
"""
def BuyTicket(ticketSelection): #set up function to get the users ticket choice
    buyRow = 0 #define the row they are buying from
    buyCol = 0 #define the column they are buying from
    selectionList = [buyRow, buyCol] #defien the table that will  hold the data for the selection
    if ticketSelection[0] == "A": #set up a system so that customers can select a ticket
        buyRow = 0
    elif ticketSelection[0] == "B": #defines the rows users can choose from
        buyRow = 1
    elif ticketSelection[0] == "C":
        buyRow = 2
    elif ticketSelection[0] == "D":
        buyRow = 3
    elif ticketSelection[0] == "E":
        buyRow = 4
        
    if ticketSelection[1] == "1": #defines the columns the user can choose from 
        buyCol = 0
    elif ticketSelection[1] == "2":
        buyCol = 1
    elif ticketSelection[1] == "3":
        buyCol = 2
    elif ticketSelection[1] == "4":
        buyCol = 3
    elif ticketSelection[1] == "5":
        buyCol = 4
    selectionList[0] = buyRow #define the row in our table as the first value
    selectionList[1] = buyCol #define the column in our table as the second value
    return selectionList #returnt the new table to the user to make changes
            
    

def main(): # definition of main program
    #Data to solve problem
    #Variables
    seatingRows = [[50, 50, 50, 50, 50], [40, 45, 45, 45, 40], [30, 35, 35, 35, 30], [20, 20, 20, 20, 20], [10, 10, 10, 10, 10]] #define the seating chart prices that the user can pick from
    columnHeader = [1, 2, 3, 4, 5]#could not implement these to work properly
    rowHeader = ["A", "B", "C", "D", "E"] #very sad to not have these as a layout
    userSelection = "" #take in the users choice for seating
    ticketCount = 5 #define that the user can only get up to 5 tickets
    currentTickets = 0 #increases each time a ticket is purchased
    removeSeat = [] #the tabke that will define what seats will be removed 
    purchasedSeat = "SS" #label that lets us know the seat is bought

        #Constants
        
  
        #Design Solution
    
    while ticketCount + 1 > currentTickets: #set up loop so that the user gets 5 chances to buy tickets
        removeSeat = [] #reset the table on each interation of the looop
        for row in range(0, len(seatingRows)):#define the rows for our table
            for col in range(0, len(seatingRows[row])): #Define the columns for the table
                print(seatingRows[row][col],sep="-", end="\t")#print the table values
        
            
            #Input
        userSelection = input("Select a Ticket by Row and Colomun \n Each Row is a Letter A-E and Column a Number 1-5 ex: A1 \n")#get the users ticket selection
        removeSeat = BuyTicket(userSelection)#call the buyticket function and return the selection in the remove seat table
        print(removeSeat) #print the selection, mainly for debugging but also so that the user knows how the grid works
        seatingRows[removeSeat[0]][removeSeat[1]] = purchasedSeat #go into our seating chart and take out the purchased seat with the remove seat tabel valuse
        currentTickets += 1 #increase the count on current bought tickets
        if currentTickets > 1: #for grammer
            print("Purchased ", currentTickets, " Tickets") #plural
        else:
            print("Purchased One Ticket")#singular
            #Process

        

        #Output
main() # execution of main program
