n = int(input())
Node = []
deg = [0]*n
parent = [-1]*n

print(print)

for i in range(n):
    l = list(map(int, input().split()))[1:]
    Node.append(l)

for i in range(len(Node)):
    deg_cnt = 0
    for j in Node[i]:
        if j != -1:
            deg_cnt+=1
            parent[j] = i
    deg[i] = deg_cnt

