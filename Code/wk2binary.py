# converting fractions to binary
# actually x can be bigger than 1
x = float(raw_input('Enter a decimal number between 0 and 1:'))
# this step is to multiply by a power of 2
# to convert into a whole number,%1 !=0 is a whole number
p = 0
while((2**p)*x)%1 != 0:
    print 'Remainder = ' + str((2**p)*x-int((2**p)*x))
    print 'p = ',p    
    p += 1
print 'p = ',p
num = int(x*(2**p))
print 'num = ',num

#same step with converting decimal to binary
result = ''
if num == 0:
    result = '0'
while num >0:
    result = str(num%2) + result
    num = num /2
print 'result = ',result
for i in range(p-len(result)+1):
    result = '0' + result
print 'result now',result

# if x=0.125,p=3,num=1,result=0001,result[0:-3]=0,result[-3:0]=001,finalresult=0.001
# if x=2.125,p=3,num=17,result=10001,result[0:-3]=10,result[-3:0]=001,final=10.001
# this step is to make sure the decimal point is put at the right place
result = result[0:-p] + '.' + result[-p:]
print 'The binary representation of the decimal ' + str(x) + ' is ' + str(result)