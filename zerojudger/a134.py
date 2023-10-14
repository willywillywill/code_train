# OK
for i in range(int(input())):
    num = int(input())
    d = num
    l = []
    s = []
    while num:
        n=0
        m=1
        while m<=num:
            m, n = m+n, m
            if l==[]:
                s.append(n)
        l.append(n)
        num -= n
    del s[0]
    s = s[::-1]
    r = [ "1" if j in l else "0"  for j in s ]

    print(d,"=","".join(r), "(fib)")
