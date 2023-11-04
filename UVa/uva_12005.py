def f(n):
    if n==1:
        return
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            ans[i] = ans.get(i,0)+1
            f(n//i)
            break
    else:
        ans[n] = ans.get(n,0)+1
import sys

for n in sys.stdin:
    n = int(n.rstrip())
    if n==0:
        break
    if n==1:
        print(1,1)
        continue
    p = n
    n = n*4-3
    ans = {}
    f(n)
    l = 1
    for i in ans:
        l *= ans[i]+1
    print(p,l)