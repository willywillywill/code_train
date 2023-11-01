
def p(x):
    k = 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            k = i
            break
    if k:
        l.append(k)
        p(x//k)


for _ in range(int(input())):
    l = []
    n = int(input())
    p(n)
    if len(l)==0:
        print(n,"is a Prime Day! ")
    else:
        print(n,"isn't a Prime Day! ")