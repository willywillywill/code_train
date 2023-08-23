"""
8
0 1 3
1 6 2
2 4 -1
3 7 5
4 -1 -1
5 -1 -1
6 -1 -1
7 -1 -1
"""


n = int(input())
l = []
for i in range(n):
    a = list(map(int, input().split()))
    l.append([a[1],a[2]])

qu = []

