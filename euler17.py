#euler16
def numstr(n):
    digits=['','one','two','three','four','five','six','seven','eight','nine',
            'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    
    numstr=''
    
    if n//1000 > 0:
        numstr = digits[n//1000]+'thousand'
    if (n%1000)//100 >0:
        numstr = numstr + digits[(n%1000)//100]+'hundred'
        if (n%1000)%100!=0:
            numstr += 'and'
    if (n%100) >= 20:
        numstr = numstr + tens[(n%100)//10]+digits[n%10]
    else:
        numstr = numstr+digits[n%20]
    return numstr

count=0    
for i in range(1,1001):
    print(numstr(i))
    count += len(numstr(i))
print(count)
    
    