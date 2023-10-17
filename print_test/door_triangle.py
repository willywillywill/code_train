
n = 2
print(" "*n+"X")
for i in range(1,n):
    print(" "*(n-i)+"X",end="")
    print(" "*(i-1)+" "+" "*(i-1)+"X")
print( *[ "X" for i in range(n+1) ])