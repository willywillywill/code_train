lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
out = 0
for i in range(len(lst1)):
    out += lst1[i]*lst2[i]
print(out)

"""
1 2 3
2 3 4
"""