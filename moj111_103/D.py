n = int(input())
l = list(map(int, input().split()))
l.sort()
k = []
for i in range(n):
    if l[i] not in l[i+1:]:
        k.append(l[i])

print(len(k))
for i in k:
    print(i, end=" ")