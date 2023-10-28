s1 = list(input())
s2 = list(input())

if (not all( [ i.isdigit() for i in s2] )) or \
            (len(s2)!=4) or \
            len(set(s2)) != 4:
    print("0A0B")
    exit()

A = 0
B = 0
for i in range(len(s1)):
    if s1[i] == s2[i]:
        A += 1
        s2[i] = ""
    elif s2[i] in s1:
        B += 1
        s2[i] = ""
    
print("%dA%dB"%(A,B))
"""
1234
3254
"""