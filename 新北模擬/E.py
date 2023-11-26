

n = int(input())
lst = list(map(int,input().split()))
A = []
K1 = []
for j in range(len(lst)):
    A.append([])
    for i in range(lst[j]+1):
        A[-1].append([i,lst[j]-i])




"""
3
11 3 3
"""