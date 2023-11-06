import math

def f(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d[i] = d.get(i,0)+1
            f(x//i)
            break
    else:
        d[x] = d.get(x,0)+1

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    d = {}
    f(a)
    a1 = "*".join([ "%s^%s"%(i,d[i]) if d[i]>=2 else str(i) for i in d ])
    a2 = math.gcd(a,b)
    d = {}
    f(a2)
    a3 = "Y" if len(d)==1 and a2 != 1 else "N"

    print("%s , %s , %s"%(a1,a2,a3))
