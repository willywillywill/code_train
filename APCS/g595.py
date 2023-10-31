
n = int(input())
lst = list(map(int,input().split()))
ans = 0
while 0 in lst:
    idx = lst.index(0)
    left = lst[idx-1] if idx-1>=0 else 99999
    right = lst[idx+1] if idx+1<n else 99999
    lst[idx] = min(left,right)
    ans += min(left,right)
print(ans)