##By listing the first six prime numbers: 2, 3, 5, 7, 11,
##and 13, we can see that the 6th prime is 13.
##What is the 10001st prime number?

def euler7(n):
    #return nth prime
    primes=[2]
    test=primes[len(primes)-1]+1
    while len(primes) < n:
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
    return primes
j = euler7(10001)

print(len(j))
print(j)
