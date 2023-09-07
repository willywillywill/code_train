# !!!
for _ in range(int(input())):

    n,m = list(map(int, input().split()))
    dit = {}

    for i in range(n,m):
        dit[i] = []
        for j in range(2, i//2+1):
            if i % j==0:
                dit[i].append(j)
    for i in dit:
        if len(dit[i])==0 and i!=1:
            print(i)