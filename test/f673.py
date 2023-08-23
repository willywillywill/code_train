

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



"""
def f(x,n=[0]):
    if x[0][0] != -1:
        x[0].pop(0)
        n[-1] += 1
        return f(x,n)
    elif x[0][1] != -1:
        x[0].pop(-1)
        n[-1] += 1
        return f(x, n)
    else:
        return n+1

print(f([0]))

"""

n = int(input())
l = []
for i in range(n):
    a = list(map(int, input().split()))
    l.append([a[1],a[2]])
ans = []
def f(x, n = []):
    if x>0:
        n.append(x)
    r = 0
    for i in l[x]:
        if i != -1:
            r += 1
            f(i, n.copy())
    if r == 0:
        ans.append(n)
f(0)
k = [ len(i) for i in ans ]
print(max(k))