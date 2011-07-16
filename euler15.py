##Euler15

def euler15(n):
    grid=[]
    for x in range(0,n+1):
        for y in range(0,n+1):
            grid.append([x,y])
    #print(grid)

    for e in grid:
        for f in grid:
            if (e[0]==f[0]) and ((e[1]==f[0] and e[0]!=f[1])or e[0]==f[1] and e[1]!=f[0]):
                print (e,f)

euler15(5)
