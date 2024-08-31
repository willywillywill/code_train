d = {"Y":0, "O":1, "X":2}

a,b = input().split()

ans = d[a]-d[b]

if ans < 0:
    print( 1 if abs(ans) == 2 else 2 )
elif ans > 0:
    print( 2 if abs(ans) == 2 else 1 )
else:
    print(ans)

