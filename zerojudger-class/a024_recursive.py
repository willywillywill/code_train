



import math
m = math.gcd(*list(map(int,input().split())))
print(m)

"""
遞迴 -> 重複呼叫自己
"""
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)