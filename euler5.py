#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#euler5


def tester(n,test):
    evens = True
    for i in range(2,n):
        if test%i!=0:
            evens = False
            break
    return evens

def euler5(n):
    test=n*(n-1)
    while True:
        if tester(n,test):
            print(test)
            break
        else:
            test+=n
        

        
 
euler5(20)
