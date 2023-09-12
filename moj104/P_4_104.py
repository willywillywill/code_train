import math

for _ in range(int(input())):

    s = list(map(int,input().split(",")))

    while len(s) != 1:
        m = []
        for i in range(len(s)-1):
            a = s.pop(0)
            b = s[0]
            m.append(math.gcd(a,b))
        s = m
        
    print(s[0])


"""
20,8,30
24,60,36
"""