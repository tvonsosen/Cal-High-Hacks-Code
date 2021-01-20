#calculates compound interest

import math

def compoundInterest(initial, rate, periods, perY):
    print("You started with: $", initial)
    result = initial * ((1+(rate/perY))**(periods))
    result = round(result,2)
    print("End Result: $", result)

def startInput():
    initialInvest = input("How much money would you like to invest initially: ")

    try:
        initialInvest = float(initialInvest)

    except:
        print('Try Again: Not a Positive Number or 0!')
        startInput()
    if initialInvest >= 0:
        pass
    else:
        print('Try Again: Not a Positive Number or 0!')
        startInput()

    running = True
    while running:
        timePeriod = input("How many years will you be earning interest: ")
        try:
            timePeriod = float(timePeriod)
        except:
            print('Try Again: Not a Positive Number or 0!')
            continue
        if timePeriod >= 0:
            running = False
        else:
            print('Try Again: Not a Positive Number or 0!')
    running = True
    while running:      
        interestRate = input("What percent interest rate are you earning yearly: ")
        try:
            interestRate = float(interestRate)
            
        except:
            print('Try Again: Not a Positive Number!')
            continue
        if interestRate >= 0:
            running = False
            interestRate = interestRate/100
        else:
            print('Try Again: Not a Positive Number or 0!')
        
    running = True
    while running:
        howOften = input("""How often are you earning interest?
Yearly, Semi-annually, quarterly, monthly, daily, or exit (y/s/q/m/d/e): """)

        if howOften == 'y':
            perYear = 1
            running = False
            totalPeriods= math.floor(timePeriod/1)
            
        elif howOften == 's':
            perYear = 2
            running = False
            totalPeriods = math.floor(timePeriod/0.5)
           
        elif howOften == 'q':
            perYear = 4
            running = False
            totalPeriods = math.floor(timePeriod/0.25)
            
        elif howOften == 'm':
            perYear = 12
            running = False
            totalPeriods = math.floor(timePeriod/0.0833)
        elif howOften == 'd':
            perYear = 365
            running = False
            totalPeriods = math.floor(timePeriod/0.0027397)
        elif howOften == 'e':
            exit()
        else:
            print('Try again! Input the lowercase keys given!')
        
    compoundInterest(initialInvest, interestRate, totalPeriods, perYear)

    again = input("Would you like to calculate again?: (y/any other key to exit) ")
    if again == 'y':
        startInput()
    else:
        exit()

startInput()
