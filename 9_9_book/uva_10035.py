s1, s2 = list(map(str, input().split()))
s1 = s1[::-1]
s2 = s2[::-1]

s1, s2 = (s1,s2+"0"*(len(s1)-len(s2))) \
            if len(s1) > len(s2) else \
                (s1+"0"*(len(s2)-len(s1)),s2)

k = 0
n = 0
for i in range(len(s2)):
    k = int((int(s1[i])+int(s2[i])) // 10) + k
    n += k

print(n)
