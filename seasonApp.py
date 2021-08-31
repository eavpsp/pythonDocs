"""
Seasons Calculator
Program Info
Elisha Victor
CSC 119 - 005
Seasons Calculator
10/17/2018
Tells the user what season it is based on the month and day
Version: Uno
"""
def main(): #definition of main program
    #Data to solve problem
    #Variables
    exitFlag = False
    month = 0
    day = 0
    season = ""
    monthName = ""
    #Constants
    #Design Solution
    while exitFlag == False:
        #Input
        month = int(input("Enter the Number of the Month: "))
        day = int(input("Enter the number of the day of the Month: "))
        
        #Process
        if month == 4 and month == 6 and month == 9 and month == 11:
            if day > 30:
                day = 30
        elif month == 2:
            if day > 28:
                day = 28
        else:
            if day > 31:
                day = 31
        #Define Months Name
        if month == 1: 
            monthName = "January"
        elif month == 2: 
            monthName = "Feburary"
        elif month == 3: 
            monthName = "March"
        elif month == 4: 
            monthName = "April"
        elif month == 5: 
            monthName = "May"
        elif month == 6: 
            monthName = "June"
        elif month == 7: 
            monthName = "July"
        elif month == 8: 
            monthName = "August"
        elif month == 9: 
            monthName = "September"
        elif month == 10: 
            monthName = "October"
        elif month == 11: 
            monthName = "November"
        elif month == 12: 
            monthName = "December"
        else:
            if month > 12:
                month = 12
                monthName = "December"
            
        #Define Months Seasons
        if month == 1 or month == 2 or month == 3:
            season = "Winter"
        elif month == 4 or month == 5 or month == 6:
            season = "Spring"
        elif month == 7 or month == 8 or month == 9:
            season = "Summer"
        elif month == 10 or month == 11 or month == 12:
            season = "Fall"
        if month % 3 == 0 and day >= 21:
            if season == "Winter":
                season = "Spring"
            elif season == "Spring":
                season = "Summer"
            elif season == "Summer":
                season = "Fall"
            else:
                season = "Winter"        
        #Output 
        print("Month: ", monthName, "\nDay: ", day, "\nSeason: ", season )
       
main() # execution of main program
