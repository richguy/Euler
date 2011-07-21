#Euler23

def divisors(n):
    l=[1]
    for i in range(2, int(n**.5+1)):
        if n%i==0:
            l.append(i)
            l.append(n//i)
    if l[len(l)-1]==l[len(l)-2]:
        del (l[len(l)-1])
    #print(l)
    if sum(l)>n:
        return l, 'Abundant'
    elif sum(l)<n:
        return l, 'Deficient'
    else:
        return l, 'Perfect'


abnums=[]
noabsum=[]
for i in range(1,28125):
    j,k = divisors(i)
    if k=='Abundant':
        abnums.append(i)

for j in range(1,28125):
    check = False
    for k in abnums:
        if abnums.count(j-k)>0 :
            check=True
            break
    if check == False:
        noabsum.append(j)
    print(j)
     
print(sum(noabsum))
    
            
