def gcd(n1,n2):
    g = 1
    n = 2
    while n<=n1 and n<=n2:
        if n1%n==0 and n2%n==0:
            g = n
        n+=1
    return g

def lcm(a,b):
    return a*b // gcd(a,b)