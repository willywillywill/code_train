str1 = input()
out = ""
for i in range(len(str1)-1):
    out += str(abs(ord(str1[i])-ord(str1[i+1])))
print(out)