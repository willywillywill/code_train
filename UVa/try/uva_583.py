max_n = 500001
p = [0]*max_n
for i in range(2,int(max_n**0.5)+1):
    if not p[i]:
        for j in range(i+i,max_n,i):
            p[j] = 1

import sys
for n in sys.stdin:
    n = int(n)
    t = False
    if n==0:
        break
    print("{} = ".format(n), end="")

    if n < 0:
        t = True
        print(-1,end="")
        n *= -1

    for i in range(2,max_n):
        if not p[i]:
           while n%i==0:
               n //= i
               if t:
                   print(" x ",end="")
               print(i,end="")
               t = True
        if n==1:
            break
    if n != 1:
        if t:
            print(" x ",end="")
        print(n,end="")
    print()

"""
2047291009
2147483648
"""