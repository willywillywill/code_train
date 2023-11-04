def f(num,fac):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            fac.append(i)
            f(num//i,fac)
            break
    else:
        fac.append(num)

while 1:
    n = int(input())
    if n==0:
        break
    if n==1:
        print(1,1)
        continue
    p = n
    n = n*4-3
    ans = 0
    facs = []
    f(n,facs)
    print(p,facs)