n1,n2 = list(map(int, input().split()))

m = 0
for n in range(n1,n2+1):
    lst_n = 1
    while n!=1:
        n = (3*n+1) if n%2 else (n/2)
        lst_n+=1
    m = max(m, lst_n)

print(m)