def euler10(n):
    #return sum of primes less than
    primes=[2]
    test=primes[len(primes)-1]+1
    while test < n:
        prime = True
        #print(test)
        for i in primes:
            if test%i==0:
                 prime=False
                 break
        if prime:
            #print (test)
            primes.append(test)
        test+=1
        
    return sum(primes)

    
print(euler10(2000000))

