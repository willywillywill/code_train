import pprint
import numpy as np
n = list(map(int, input().split(",")))

A = []
B = []
AB = []
xy = {}
for i in range(n[0]):
    k = list(map(str, input().split()))
    if 9999 in k:
        xy["A"] = [i,k.index(9999)]
    A.append(k)
for i in range(n[2]):
    k = list(map(str, input().split()))
    if 9999 in k:
        xy["B"] = [i,k.index(9999)]
    B.append(k)
for i in range(n[0]):
    k = list(map(str, input().split()))
    if 9999 in k:
        xy["AB"] = [i,k.index(9999)]
    AB.append(k)




"""
2,3,3,4 
1 2 9999
0 -4 1 
3 1 0 2 
-1 2 5 0 
0 -2 2 1 
1 -1 16 5 
4 -10 -18 1


4,3,3,5 
2 4 1 
3 6 2 
2 5 0 
1 2 3 
2 6 2 0 2 
3 1 1 1 2 
9999 2 2 0 1 
20 18 10 4 13 
32 28 16 6 20 
19 17 9 5 14 
20 14 10 2 9
"""