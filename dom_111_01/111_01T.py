lst = input().split(",")
def dfs(i,l):
    if lst[i-1]=="null":
        return
    l.append(lst[i-1])

    if 2*i <= len(lst):
        dfs(2*i,l.copy())
    if 2*i+1 <= len(lst):
        dfs(2*i+1, l.copy())
    else:
        for j in range()
        ans.add(tuple(l))
ans = set()
dfs(1,[])

print(ans)

"""
1,2,3,null,5
1,2,3,null,4,5,6,null,null,7
"""