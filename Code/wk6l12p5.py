def genPrimes():
    primeList = []
    x = 1
    while x < 10000:
        x += 1
        for p in primeList:
            if x % p == 0:
                break
        # loop statements may have an else clause; 
        # else is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while)
        # but not when the loop is terminated by a break statement 
        # so else means no break
        else:
            primeList.append(x)
            yield x

        
prime = genPrimes()
print prime.next()  
print prime.next()
print prime.next()
print prime.next()
print prime.next()
print prime.next()
print prime.next()


