#The following iterative sequence is defined for the set of positive integers:

#n->  n/2 (n is even)
#n->  3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13  40  20  10  5  16  8  4  2  1
#It can be seen that this sequence (starting at 13 and finishing at 1)
#contains 10 terms. Although it has not been #proved yet (Collatz Problem),
#it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

def sequence(n):
    c=[n]
    while c[-1]!=1:
        if c[-1]%2==0:
            c.append(c[-1]//2)
        else:
            c.append(c[-1]*3+1)
        #print(c)
    return len(c)

def euler14(n):
    maxlen = 0
    maxlennum = 0
    for i in range(1,n):
        if sequence(i)>maxlen:
            maxlen, maxlennum = sequence(i), i
    return maxlen, maxlennum
        
print(euler14(1000000))
