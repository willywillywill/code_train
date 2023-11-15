# height 2xLoop  (0.6s)
def f(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
p = [ i for i in range(50000) if f(i)  ]

""" low  3xLoop  (4.8s)
max_n = 50000
p = [0]*max_n
p[0],p[1] = 1,1
for i in range(2,int(max_n**0.5)+1):
    if p[i]:
        for j in range(i+i,max_n,i):
            p[j] = 1
p = [ i for i in range(len(p)) if not p[i] ] 
"""

import sys
for n in sys.stdin:
    n = int(n)

    l = []
    if n==0:
        break

    print( "{} = ".format(n),end="" )
    if n < 0:
        l.append("-1")
        n *= -1

    for i in range(len(p)):
        while n%p[i] == 0:
            n //= p[i]
            l.append(str(p[i]))
        if n==1:
            break
    else:
        l.append(str(n))

    print(" x ".join(l))


"""
2047291009
2147483648

2147483548

2147483647

499979
"""