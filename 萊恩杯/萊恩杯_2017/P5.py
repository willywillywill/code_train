s = input()
ans = []
for i in range(len(s)):
    l = []
    for j in range(i,len(s)):
        if s[j] in l:
            ans.append(l.copy())
            break
        l.append(s[j])
ans.sort(key=lambda x:len(x),reverse=True)
print("".join(ans[0]),len(ans[0]))
"""
abcdabcdbb
"""