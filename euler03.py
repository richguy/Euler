#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def prime(n): #Checks if a given number is prime
	prime = 0
	for i in range ((n+1)/2, 2, -1):
		if n%i == 0:
			prime = i
			break
	return prime

def erats(n):
    # Create a candidate list within which non-primes will be
    # marked as None; only candidates below sqrt(n) need be checked. 
    candidates = list(range(n+1))
    fin = int(n**0.5)
 
    # Loop over the candidates, marking out each multiple.
    for i in range(2, fin+1):
        if candidates[i]:
            # from 2i in steps of i, set each to None
            candidates[2*i::i] = [None] * len(candidates[2*i::i])
 
    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]

print (erats(6008))
