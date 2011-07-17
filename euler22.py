#euler22
def makelist():
    names=[]
    f = open('names.txt','r')
    for line in f:
        t=line.split('","')
        ##Clean up first and last entries
        t[0]=t[0][1:len(t[0])]
        t[len(t)-1]=t[len(t)-1][0:len(t[len(t)-1])-1]

        return sorted(t)

def alphaval(s):
    av=0
    for c in s:
        av+=ord(c)-64
    return av

k=makelist()
v=0
for i in range(0,len(k)):
    v+=alphaval(k[i])*(i+1)
print(v)

