s = input()
ans = 0

for i in range(len(s)):
    lst = []
    for j in range(i,-1,-1):
        lst.append(s[j])
        if lst[::-1]==lst:
            ans = max(ans,len(lst))

print(ans)

"""
123batabba321
"""