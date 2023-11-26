s = input()
ans = 0
for i in s:
    ans += int(i)**len(s)
print(str(ans)==s)