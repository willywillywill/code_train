n = int(input())-1
ans = [0,0,0]
if n>=7500:
    n -= 7500
    ans[0] = 3
    ans[1] = n//25 +1
    ans[2] = n%25 +1
elif n>=2500:
    n -= 2500
    ans[0] = 2
    ans[1] = n//50 +1
    ans[2] = n%50 +1
else:
    ans[0] = 1
    ans[1] = n//25 +1
    ans[2] = n%25 +1
print(*ans)