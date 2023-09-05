import pprint
import numpy as np
n = list(map(int, input().split(",")))

A = []
B = []
AB = []
xy = {}
for i in range(n[0]):
    k = list(map(int, input().split()))
    if 9999 in k:
        xy["A"] = [i,k.index(9999)]
    A.append(k)
for i in range(n[2]):
    k = list(map(int, input().split()))
    if 9999 in k:
        xy["B"] = [i,k.index(9999)]
    B.append(k)

for i in range(n[0]):
    k = list(map(int, input().split()))
    if 9999 in k:
        xy["AB"] = [i,k.index(9999)]
    AB.append(k)

if "A" in xy:
    ans = AB[xy["A"][0]][::]
    A_ = A[xy["A"][0]][::]
    B_ = [ [ B[i][j] for i in range(len(B)) ] for j in range(len(B[0])) ]
    k = {}
    for i in range(len(B_)):
        s = 0
        for j in range(len(A_)):
            s+= A_[j]*B_[i][j]
            if B_[i][j] != 0 and A_[j] == 9999:
                k[AB[xy["A"][0]][j+1]] = B_[i]
    
    c2 = list(k.keys())[0]
    c3 = k[c2]

    a = 0
    d = 0
    for i in range(len(A_)):
        if A_[i] != 9999:
            a+= A_[i]*c3[i]
        else:
            d = c3[i]
    a = c2-a
    print(int(a/d))
else:
    ans = AB[xy["B"][1]][::]
    A_ = A
    B_ = B[xy["B"][1]]
    k = {}

    for i in range(len(A_)):
        s = 0
        for j in range(len(B_)):
            s+= B_[j]*A_[i][j]
            if A_[i][j] != 0 and B_[j] == 9999:
                k[AB[xy["B"][1]][j+1]] = A_[i]

    print(A_)
    print(B_)
    print(k)
    print(s)


"""
2,3,3,4 
1 9999 3
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