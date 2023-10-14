# OK

""" Bing """
def f(n):
    if n==1:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

def f_hz(s):
    dit = {}

    for c in s:
        dit[c] = dit.get(c, 0) + 1

    primes = [c for c in dit if f(dit[c])]
    primes.sort()
    return ''.join(primes) if primes else 'empty'

for i in range(int(input())):
    s = input()
    print("Case %d:"%(i+1), f_hz(s))

""" Me """

def f(n):
    l = []
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    return l

for _ in range(int(input())):

    s = input()
    dit = {}
    l = []

    for i in s:
        if i in dit.keys():
            dit[i] += 1
        else:
            dit[i] = 1
    print("Case %d: "%(_+1), end="")

    for i in dit.keys():
        v = dit[i]
        if not f(v):
            if v > 1:
                l.append(i)
    if l:
        l.sort()
        print("".join(l))
    else:
        print("empty")