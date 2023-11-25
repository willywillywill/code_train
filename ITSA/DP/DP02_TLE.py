
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = set()

for i in range(1<<n):
    x = sum(a[j] for j in range(n) if i & (1<<j))
    s.add(x)
print(s)



"""
1 5
1
1 2 3 4 5


2
2 5
3 5
1 5 2 7 8
3 5
2 5 2
20 1 2 4 9
"""