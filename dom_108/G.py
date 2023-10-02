

edge_number = int(input())
val = [0]* edge_number
val[0] = 1
dit = {}
for i in range(int(input())):
    a,b = list(map(int,input().split()))
    if a in dit:
        dit[a].append(b)
    else:
        dit[a] = [b]
    if b in dit:
        dit[b].append(a)
    else:
        dit[b] = [a]

def f(px,x):
    for i in dit[x]:
        if i != px and val[i]==0:
            val[i] = val[x]+1
            f(x,i)

f(0,0)
print(val)

"""
5
10
0 1
0 2
0 3
0 4
1 2
1 3
1 4
2 3
2 4
3 4

4
4
0 1
1 2
2 3
3 0
"""