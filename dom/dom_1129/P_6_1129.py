s = input().split(",")

for i in range(len(s)):
    if s[i] == "0":
        k = s.pop(i)
        s.append(k)
print(",".join(s))
