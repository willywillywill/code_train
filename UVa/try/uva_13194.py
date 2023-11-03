def p(x, l):
    global ans
    k = 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            k = i
            break
    print(x)
    if k:
        l.append(k)
        p(x//k, l.copy())
    else:
        l.append(x)
        ans = l


ans = []
n = 999900007063
p(n,[])
print(ans)
if sum(ans)==n:
    print("perfect")
elif sum(ans) < n:
    print("deficient")
else:
    print("abundant")