n,m = input().split()
A = 0
B = 0
for i in range(4):
    if n[i]==m[i]:
        A += 1
    elif n[i] in m:
        B += 1
print("%sA%sB"%(A,B))
"""
1235 4385
"""