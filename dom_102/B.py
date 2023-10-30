
for _ in range(int(input())):
    dit = {}
    for i in range(int(input())):
        for j in map(int,input().split(",")):
            dit[j] = dit.get(j,0)+1

    lst = list(dit.items())
    lst.sort(key=lambda x:x[1],reverse= True)
    m = lst[0][1]
    lst = [ str(lst[i][0]).rjust(2,"0") for i in range(len(lst)) if lst[i][1]==m ]
    print(",".join(lst))
    print()

"""
2
4
01, 07, 29, 30, 35
01, 07, 29, 30, 36
07, 22, 23, 24, 25
01, 22, 23, 24, 25
2
01, 07, 29, 30, 35
01, 07, 29, 30, 37
"""