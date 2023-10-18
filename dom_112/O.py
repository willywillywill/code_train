
p,d = list(map(int,input().split()))
ans = 0
if d%p:
    ans = d//2
else:
    ans = d//2-1
print(ans)
