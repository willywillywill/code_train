w = int(input())
n = int(input())
tw = 0
tl = 0
for i in range(n):
    l = list(map(int,input().split()))
    tw+=l[0]
    tl+=l[1]

print(tw,tl)

"""
4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1
"""