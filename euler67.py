#euler67
def maketri():
    tri=[]
    f = open('triangle.txt','r')
    for line in f:
       tri.append([int(x) for x in line.split()])
    return tri
        
    

tri=maketri()

for i in range(len(tri)-2, -1, -1):
    for j in range(0,len(tri[i])):
        #print(tri[i][j], tri[i+1][j],tri[i+1][j+1])
        if tri[i][j]+ tri[i+1][j] > tri[i][j]+tri[i+1][j+1]:
            tri[i][j]+=tri[i+1][j]
        else:
            tri[i][j]+=tri[i+1][j+1]

print(tri[0][0])


