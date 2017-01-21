# use bisection search to make the program faster
balance = 999999
epsilon = 0.01
newBal = balance
annualInterestRate = 0.18
lowerB = balance / 12.0
upperB = (balance * ((1 + annualInterestRate / 12) ** 12)) / 12.0
pay = (lowerB + upperB) / 2
# bisecion got to have an episilon
while abs(newBal) >= epsilon :
    newBal = balance
    for i in range(12):
        unpayBal = newBal - pay
        newBal = unpayBal * (1 + annualInterestRate / 12.0 )
    if newBal > 0:
        lowerB = pay
    if newBal < 0:
        upperB = pay 
    
    pay = (lowerB + upperB) / 2

print 'Lowest Payment:', round(pay,2)
       