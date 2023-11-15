
for _ in range(int(input())):
    x,a,b = map(int,input().split())

    cntA = x//a
    while (x-cntA*a)%b !=0 and cntA>=0:
        cntA -= 1
    if cntA < 0:
        print(-1)
    else:
        cntB = (x-cntA*a)//b
        print(cntA+cntB)
