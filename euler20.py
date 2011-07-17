import math

def euler20(n):
    s=0
    n=str(math.factorial(n))
    for i in n:
        s+=int(i)
    return s

print(euler20(100))
        
