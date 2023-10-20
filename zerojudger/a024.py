def gcd(n,m):
    if n<m:
        return gcd(m,n)
    return gcd(m,n%m) if m else n
lst = list(map(int,input().split()))
print(gcd(lst[0],lst[1]))

"""
import math
print(math.gcd(lst[0],lst[1]))
"""