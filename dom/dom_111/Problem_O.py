import itertools

n, m = list(map(int, input().split()))
k = list(map(int, input().split()))

g = m//min(k)
k = k*g
lst = []
print(g,k)

for i in range(1,g+1):
    for j in itertools.combinations(k,i):
        if sum(j)==m:
            if sorted(list(j)) not in lst:
                lst.append(sorted(list(j)))
print(len(lst))