"""
2 3
3 1 2
8 5 4
> 90+LR

3 8
1 5
2 4

rxc -> cxr

"""

r,c = map(int,input().split())
l = []
for _ in range(r):
    l.append(list(map(int,input().split())))

for i in range(c):
    for j in range(r):
        print(l[j][i], end=" ")
    print()



