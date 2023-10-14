#

dit = {}
for _ in range(int(input())):
    s = list(map(str, input().split()))
    s = s.pop(0)
    dit[s] = dit.get(s, 0)+1


for i in sorted(dit):
    print(i,dit[i])
    

