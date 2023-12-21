s = input().split("+")
for i in range(len(s)):
    s[i] = eval(s[i])
s = str(sum(s))
if len(s)>4:
    ss = s[-4:]
    if ss[0]=="0":
        ss = ss[1:]
else:
    ss = s
print(ss)