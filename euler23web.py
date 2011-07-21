#!/usr/bin/env python

'''Project Euler - Problem 23
"Find the sum of all the positive integers which cannot be 
written as the sum of two abundant numbers."'''
def sum_divisors(n):
    """Sums the proper divisors of n."""
    sum = 1
    for x in range(2, int(n ** 0.5) + 1):
        if (n % x == 0):
            sum += x + n / x
    if (n ** 0.5) == int(n ** 0.5): sum -= (n ** 0.5)
    return sum

def is_abundant(n):
    """Checks if the sum of the divisors of n is greater than n."""
    if sum_divisors(n) > n: 
        return True
    else: return False

def find_abundants(limit):
    """Finds all abundant numbers up to the specified limit"""
    abundants = [x for x in range(1, limit) if is_abundant(x)]
    return abundants

def get_list(limit):
    abds = find_abundants(limit)
    l = list(range(limit))
    for x in abds:
        for y in abds:
            if x + y >= limit:
                break
            l[x + y] = 0
    return l

print(sum(get_list(28123)))
