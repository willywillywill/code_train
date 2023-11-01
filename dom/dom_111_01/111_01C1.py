p = lambda x: not len([ i for i in range(2,int(x**0.5)+1) if x%i==0 ])
while 1:
    n = int(input())
    if not n:
        break
    ans = 0
    for i in range(2,int(n*0.5)+1): # 1/2 times
        if p(i) and p(n-i): # ! ! ! ex: n=(n-i)+(i)
                            #       if (n-1 and i) is premi
                            #       -> ans+=1

            ans+=1
    print(ans)

"""
8
20
42
10
12
4
0
"""