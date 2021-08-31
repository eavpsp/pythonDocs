"""
Psuedo Loop Trace
Program Info
Elisha Victor
CSC 119 - 005
Psuedo Loop Trace
10/17/2018
follow the trace
Version: Uno
"""
def main(): #definition of main program
    #Data to solve problem
    #Variables
    i = 0
    j = 10
    n = 0

    k = 0
    l = 0
    m = 0
    #Constants
    
        #Design Solution
    print("LoopTraceA: \n")
    while i < j :
        i = i + 1
        j = j - 1
        n = n + 1
        print("N: ", n, "I: ", i, "J: ", j)
        #Input
    print("LoopTraceB: \n")    
    while k < 10:
        k = k + 1
        m = m + k + l
        l = l + 1
        print("I: ", k, "N: ", m, "J: ", l)
        
        #Process
        
        #Output 
    
main() # execution of main program
