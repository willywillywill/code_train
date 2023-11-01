n = int(input())
if n//12:
    ans = 0
    k = n//12
    n -= k*12
    ans += k*50
    ans += n*5
    print(ans)
else:
    print(n*5)