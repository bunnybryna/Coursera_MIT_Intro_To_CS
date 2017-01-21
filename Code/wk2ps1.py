# this program counts up the number of vowels contained in the string s
s = 'hello'
count = 0
for i in s:
    if i in 'aeiou':
        count += 1
print count

# this program prints the number of times the string 'bob' occurs in s
# s = 'boobobbo hobobobthehobowonder'
# s = 'giuboobobobbobbboobgobbobbobobooboblpty'
s = 'bobobbcoobbobob'
count = 0
ls = len(s)
#len('bob')=3
for a in range((ls-3+1)):
    i = s[a:a+3]
    if i == 'bob':
        count += 1
print 'Number of times bob occurs is: ', count 

# write a function called item_order that takes as input a string named order
def item_order(order):
    saladNum = 0
    hamNum = 0
    waterNum = 0
    list = order.split()
    print list
    for i in list:
            if i == 'salad':
                saladNum += 1
            elif i == 'hamburger':
                hamNum += 1
            else:
                waterNum += 1
    print 'salad',saladNum
    print 'hamburger',hamNum
    print 'water',waterNum
    return 'salad:' + str(saladNum) + ' ' + 'hamburger:' + str(hamNum) + ' ' + 'water:' + str(waterNum)
print item_order("salad water hamburger salad hamburger")
# should use return instead of print 
# print is a function, when you print print someVariable
# you will get None as the second part because the return value of print is None.
    
# second version using .count()
def item_order2(order):
    saladNum = order.count('salad')
    hamNum = order.count('hamburger')
    waterNum = order.count('water')
    print 'salad',saladNum
    print 'hamburger',hamNum
    print 'water',waterNum
    return 'salad:' + str(saladNum) + ' ' + 'hamburger:' + str(hamNum) + ' ' + 'water:' + str(waterNum)
print item_order2("salad water hamburger salad hamburger")
