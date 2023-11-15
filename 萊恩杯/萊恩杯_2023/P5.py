from itertools import combinations_with_replacement,permutations

n,m = map(int,input().split())
ans = []
data = [ i for i in range(1,n+1) ]
for i in range(1,m+1):
    t = list(combinations_with_replacement(data,i))
    for j in t:
        if sum(j)==n:
            lst = list(set(list(permutations(j))))
            ans += lst

print(len(ans))