s = input()
out = ""
for i in range(1,len(s)):
    out += str(abs(ord(s[i-1])-ord(s[i])))
print(out)