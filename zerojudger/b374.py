input()
lst = list(map(int,input().split()))
dit = {}
for i in lst:
    dit[i] = dit.get(i,0)+1

lst = list(dit.items())
lst.sort(key=lambda x:(x[1],x[0]))


m = lst[-1][1]
for i in lst:
    if i[1] == m:
        print(i[0],i[1])
        