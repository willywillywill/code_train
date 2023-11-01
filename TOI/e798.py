lst = []
out = []
for _ in range(int(input())):
    lst.append(list(map(int,input().split())))

for i in range(0,len(lst),2):
    out.append([])
    for j in range(0,len(lst[0]),2):
        l = lst[i][j:j+2]+lst[i+1][j:j+2]
        out[-1].append(max(l))

for i in out:
    print(*i)

"""
4
12 20 30 0
8 12 2 0
34 70 37 4
112 100 25 12
"""