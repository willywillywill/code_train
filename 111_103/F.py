s1 = list(input())
s2 = list(input())

while s2:
    k = s2[0]
    if k in s1:
        del s1[s1.index(k)]
    else:
        del s2[0]
print("".join(s1))