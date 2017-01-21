# p1 calculate credit card balance after one year if pays the minimum monthly each month
balance = 4574
annualInterestRate = 0.18
monthlyPaymentRate = 0.05
month = 0
total = 0
# new balance = remainBal is the key to form the loop
for i in range(12):
    minPay = balance * monthlyPaymentRate
    unpayBal = balance - minPay
    remainBal = unpayBal + annualInterestRate / 12.0 * unpayBal 
    balance = remainBal
    total += minPay
    month += 1
    print 'Month: ', month
    print 'Minimum monthly payment: ', round(minPay,2)
    print 'Remaining balance: ', round(remainBal,2) 
print 'Total paid: ', round(total,2)
print 'Remaining balance', round(remainBal,2)
    
# p2,calculates the minimum fixed monthly payment to pay off a credit card balance within 12 months
# wrong code # 1
# I was stuck because I want to construct two loops
# but both increment varialbe(balance and fixPay) are changing 
# one for loop to increment fixPay, the other to increment balance
# and a if statement to test balance12 <= 0
balance = 3329
annualInterestRate = 0.2
month = 0
totalInterest = 0 
fixPay = 10
while 12 * fixPay - balance - totalInterest > 0:
    for m in range(12):
        unpayBal = balance - fixPay
        monthInterest = annualInterestRate / 12.0 * unpayBal
        remainBal = unpayBal + monthInterest
        balance = remainBal
        totalInterest += monthInterest
        month += 1 
    print 'Month: ', month
    print 'Total interest: ', round(totalInterest,2)
    print 'Remaining balance: ', round(remainBal,2)
    fixPay += 10 
    print 'Lowest Payment,' fixPay

# wrong code # 2
# line 60, balance is a constant,if I set balance = newBal
# then next step in the while loop,newBal will not be 4773, but will be last newBal
# if the balance is always change, newBal after 12 months will be always positive  
# will cause an infinite loop   
balance = 4773
annualInterestRate = 0.2
fixPay = 0
while balance > 0:
    month = 0
    newBal = balance
    fixPay += 10
    for i in range(12):
        unpayBal = newBal - fixPay
        newBal = unpayBal * (1 + annualInterestRate / 12.0 )
        month += 1
        print  'In the month,',month,' there will be ', newBal, 'left'
    balance = newBal
print 'Lowest Payment:', fixPay
        
# right code
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