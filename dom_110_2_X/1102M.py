
a,b,c,d = list(map(int,input().split()))
arr1 = []
arr2 = []
ans = []
for _ in range(a):
    arr1.append(list(map(int,input().split())))
for _ in range(c):
    arr2.append(list(map(int,input().split())))


for i in range(a): # arr1 -> x
    for j in range(c): # arr2 -> x
        ans.append([])
        for k in range(b): # arr1 -> y
            for l in range(d): # arr2 -> y
                ans[-1].append(arr1[i][k]*arr2[j][l])
for i in ans:
    print(*i)

"""
2 2 2 2
1 2
3 1
0 3
2 1
"""