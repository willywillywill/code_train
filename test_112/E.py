n = int(input())
lst = list(map(int,input().split()))
dit = {}
for i in lst:
    dit[i] = dit.get(i,0)+1
v = max(set(dit.values()))
out = [ i for i in dit if dit[i]==v ]
out.sort()
print(*out)

"""
13
1 5 3 9 1 4 0 0 0 1 4 2 4

11
0 1 2 3 4 5 6 7 8 9 1
"""