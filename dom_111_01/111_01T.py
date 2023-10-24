lst = input().split(",")

def dfs(i,l):
    if lst[i-1] == "null":
        return
    k = 1
    l.append(lst[i-1])
    if 2*i <= len(lst):
        k = 0
        dfs(2*i,l.copy())
    if 2*i+1 <= len(lst):
        k = 0
        dfs(2*i+1,l.copy())
    if k:
        print("->".join(l))

dfs(1,[])

"""
1,2,3,null,5
1,2,3,null,4,5,6,null,null,7

?
1,2,3,null,null
"""