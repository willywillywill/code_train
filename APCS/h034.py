lst = []
n = int(input())
m = 0
for _ in range(n):
    lst.append(list(input()))
    m = max(len(lst[-1]), m)
a = []

for i in range(m):
    for j in range(n):
        if i < len(lst[j]):
            if lst[j][i].isalpha():
                a.append(lst[j][i])
print("".join(a))


"""
3
AB
CIDJ
RKE
"""