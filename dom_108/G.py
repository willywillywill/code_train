
edge_number = int(input())
nodes_clr = [0]*edge_number
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
for i in dit:
    k = [ nodes_clr[ii] for ii in dit[i] ]
    if sorted(k)[-1] == sorted(k)[0]:
        nodes_clr[i]=1
    else:
        nodes_clr[i]=max(k)+1


print(nodes_clr)


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