import pprint

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
    ans = {}
    a = []
    for i in range(len(AB[xy["A"][0]])):
        ans[ AB[xy["A"][0] ][i] ] = []
        for j in range(n[1]):
            c = [A[xy["A"][0]][j], B[j][i]]
            if 0 not in c and 9999 in c:
                a = AB[xy["A"][0] ][i]
            ans[ AB[xy["A"][0] ][i] ].append( c )
    d = 1
    sx = 0
    num = 0
    for i in ans[a]:
        if 9999 not in i:
            sx+= i[0]*i[1]
        else:
            num = i[1] if i[0]==9999 else i[0]
    print(int((a-sx)/num))
else:
    ans = {}
    a = []
    for i in range(len(AB[xy["B"][0]])):
        ans[ AB[xy["B"][0] ][i] ] = []
        for j in range(n[1]):
            print(A[xy["B"][0]][0], B[j][xy["B"][1]])

print(a)
print(ans)

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