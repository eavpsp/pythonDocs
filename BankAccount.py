"""
    BankAccountCalculator
    Program Info
    Elisha Victor
    CSC 119 - 005
    Bank Account Calculator
    08/29/2018
    Calculating 3 years of having 1000$ with 5 percent interest per year.
    Version: Uno
"""
def main(): # definition of the main program
    # Data to solve problem
    bankAccountBalance = 1000.00
    bankAccountBalanceYear2 = 0.00
    bankAccountBalanceYear3 = 0.00
    INTEREST_PER_YEAR = 0.05
    # Design Solution
    # Input / data coming in to program
    # Process
    bankAccountBalanceYear2 = (bankAccountBalance * INTEREST_PER_YEAR) + bankAccountBalance
    bankAccountBalanceYear3 = (bankAccountBalanceYear2 * INTEREST_PER_YEAR) + bankAccountBalanceYear2
    # Output / answer to problem
    welcomeMessage = "Welcome to the Bank Account Calculator"
    yearOneMessage = "Your account balance in 2018 after your 5% interest is: $"
    yearTwoMessage = "Your account balance in 2019 after your 5% interest is: $"
    yearThreeMessage = "Your account balance in 2020 after your 5% interest is: $"
    print (welcomeMessage)
    print (yearOneMessage, "%.2f" % bankAccountBalance)
    print(yearTwoMessage, "%.2f" % bankAccountBalanceYear2)
    print(yearThreeMessage, "%.2f" % bankAccountBalanceYear3)
main() # execution of main program
