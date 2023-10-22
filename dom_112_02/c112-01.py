ans = 0
s = input()
for i in range(len(s)):
    lst = []
    for j in range(i,-1,-1):
        if s[j] not in lst:
            lst.append(s[j])
        else:
            break
    ans = max(len(lst),ans)
print(ans)

"""
babcAbcbb
"""