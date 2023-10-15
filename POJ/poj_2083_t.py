def p(i,x,y):
    if i==1:
        lst[x][y] = "X"
        return
    p(i-1, x,y)
    p(i-1, x,y+2*m)
    p(i-1, x+m,y+m)
    p(i-1, x+2*m,y)
    p(i-1, x+2*m,y+2*m)

n = 4
m = 3**(n-2)
lst = [[ 0 for i in range(100) ] for i in range(100)]
p(n,1,1)
t = 0
for i in lst:
    for j in i:
        if j:
            print("X",end="")
        else:
            print(" ",end="")
    print()