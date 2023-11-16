s = input()
z = 1
o = 1
max_z = 0
max_o = 0
for i in range(1,len(s)):
    if s[i]==s[i-1]=="0":
        z += 1
    else:
        z = 1
    max_z = max(z,max_z)

    if s[i]==s[i-1]=="1":
        o += 1
    else:
        o = 1
    max_o = max(o,max_o)
print(abs(max_z-max_o))