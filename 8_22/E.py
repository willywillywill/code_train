n = int(input())
l = list(map(int, input().split()))
l.sort()
dit = {}
for i in range(n):
    dit[l[i]] = dit.get(l[i], 0)+1

for i in dit:
    print(i, dit[i])