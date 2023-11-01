lst = input().split(",")

def dfs(i,l):
    if lst[i] == "null":
        return
    k = 1
    l.append(lst[i])
    if 2*i+1 < len(lst):
        if lst[2*i+1] != "null":
            k = 0
            dfs(2*i+1,l.copy())
    if 2*i+2 < len(lst):
        if lst[2*i+2] != "null":
            k = 0
            dfs(2*i+2,l.copy())
    if k:
        print("->".join(l))

dfs(0,[])

"""
1,2,3,null,5
1,2,3,null,4,5,6,null,null,7

?
1,2,3,null,null
"""