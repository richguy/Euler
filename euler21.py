#euler21

def divisors(n):
    l=[1]
    for i in range(2, int(n**.5+1)):
        if n%i==0:
            l.append(i)
            l.append(n//i)
    if l[len(l)-1]==l[len(l)-2]:
        del (l[len(l)-1])
    #print(l)
    return l

def dsum(n):
    return sum(divisors(n))
l=[]
for i in range(1,10001):
    if i==dsum(dsum(i)) and i!=dsum(i):
        print(i, dsum(i), dsum(dsum(i)))
        l.append(i)
        l.append(dsum(i))

print(sum(list(set(l))))
