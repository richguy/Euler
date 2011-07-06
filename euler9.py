##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

def euler9():
    c=0
    for a in range(1,1000):
        for b in range(a+1,1000):
            c = 1000-a-b
            #print(a,b,c,)
            #print(a**2, b**2, c**2)
            if (c<=b) or (c<0)or (a**2+b**2!=c**2):
                continue
            else:
                print(a,b,c)
                print(a*b*c)

euler9()
