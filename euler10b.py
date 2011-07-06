#euler10b sieve method
#Find sum of primes under 2 000 000
def euler10b(n):
    # Create a candidate list within which non-primes will be
    # marked as None; only candidates below sqrt(n) need be checked. 
    candidates = list(range(n+1))
    end = int(n**0.5)
 
    # Loop over the candidates, marking out each multiple.
    for i in range(2, end+1):
        if candidates[i]:
            # from 2i in steps of i, set each to None.
            candidates[2*i::i] = [None] * len(candidates[2*i::i])
 
    # Filter out non-primes and return the list.
    return sum([i for i in candidates[2:] if i])
print(euler10b(2000000))
