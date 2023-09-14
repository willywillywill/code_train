def f(n):
    if n%2==1:
        ans1.append(n)
    else:
        ans2.append(n)
    if n>0:
        f(n-1)

ans1 = []
ans2 = []
f(10)
print(ans1)
print(ans2)