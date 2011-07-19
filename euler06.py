##The sum of the squares of the first ten natural numbers is,
##
##1^2 + 2^2 + ... + 10^2 = 385
##The square of the sum of the first ten natural numbers is,
##
##(1 + 2 + ... + 10)^2 = 55^2 = 3025
##Hence the difference between the sum of the squares of the first
##ten natural numbers and the square of the sum is 3025  385 = 2640.
##
##Find the difference between the sum of the squares of the first
##one hundred natural numbers and the square of the sum.

def euler6(n):
    
    sumofsqrs=0
    
    for i in range(1,n+1):
        sumofsqrs += i**2
    return (sum(range(1,n+1))**2)-sumofsqrs

print(euler6(100))
    
        
