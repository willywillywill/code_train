dit = {}
edge_number = int(input())
for i in range(int(input())):
    a,b = list(map(int,input().split()))
    if a in dit:
        dit[a].append(b)
    else:
        dit[a] = [b]

print(dit)

"""
3
3
0 1
1 2
2 0

9
8
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8 
"""