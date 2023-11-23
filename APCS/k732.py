
n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if (i+j)%10==lst[i][j]:
            print(i,j)

"""
1 8
1 2 3 4 5 6 7 8
"""