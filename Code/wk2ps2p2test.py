balance = 4773
newBal = balance
annualInterestRate = 0.2
fixPay = 0
while newBal > 0:
    month = 0
    newBal = balance
    fixPay += 10
    for i in range(12):
        unpayBal = newBal - fixPay
        newBal = unpayBal * (1 + annualInterestRate / 12.0 )
        month += 1
        print  'In the month,',month,' there will be ', newBal, 'left'

print 'Lowest Payment:', fixPay
       