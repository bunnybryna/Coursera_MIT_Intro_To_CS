# p2,calculates the minimum fixed monthly payment to pay off a credit card balance within 12 months
balance = 4773
newBal = balance
annualInterestRate = 0.2
fixPay = 0
while newBal > 0:
    # need to set month = 0
    # this line is vey important, it will reset newBal to a constant before every time fixpay increases to a new number
    newBal = balance
    fixPay += 10
    for i in range(12):
        unpayBal = newBal - fixPay
        newBal = unpayBal * (1 + annualInterestRate / 12.0 )
        # no need month += 1
        # print  'In the month,',month,' there will be ', newBal, 'left'
        # now, if newBal after 12 months <0, the while loop will break

print 'Lowest Payment:', fixPay
       

