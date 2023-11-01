txt = [chr(i) for i in range(97, 123)]+[chr(i) for i in range(65, 65+26)]



s = input()
ans = 0
for i in range(len(s)):
    lst = [999999]
    for j in range(i,-1,-1):
        if txt.index(s[j]) < lst[-1]:
            lst.append(txt.index(s[j]))
            ans = max(ans, len(lst))
        else:
            break
print(ans-1)

"""
daeKMPRwz
aaabce
"""