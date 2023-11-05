"""
while 1:
    try:
        n,k = list(map(int,input().split()))
        s = n
        while n >= k:
            s += n//k
            n = (n//k)+(n%k) # <- (n%k) 剩下的
        print(s)
    except:
        break
"""

def f(x):
    if x >= k:
        return f(x//k+n%k)+x//k
    return x//k

while 1:
    try:
        n,k = list(map(int,input().split()))
        print(f(n)+n)
    except:
        break