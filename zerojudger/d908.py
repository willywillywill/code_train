root = ord(input())-ord("A")
graph = [ [0]*26 for _ in range(26) ]
vis = {}
val = {}
for i in range(int(input())):
    a,b,v = input().split()
    graph[ord(a)-ord("A")][ord(b)-ord("A")] = int(v)
    vis[ord(a)-ord("A")] = 0
    vis[ord(b)-ord("A")] = 0
    val[ord(a)-ord("A")] = 0
    val[ord(b)-ord("A")] = 0

qu = [root]
while qu:
    qu.sort(key=lambda x:val[x],reverse=True)
    for i in qu: print(val[i],end=" ")
    print()
    idx = qu.pop(0)
    if vis[idx]:
        continue
    vis[idx] = 1
    for i in range(26):
        if graph[idx][i]:
            val[i] = max(val[idx]+graph[idx][i],val[i])
            qu.append(i)

print(max(val.values()))


"""
A
3
A B 2
A C 3
B C 5
"""