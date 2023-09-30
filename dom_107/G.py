# DFS Bottom-up

class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(i):
    root = node(in1[i])
    nodes.add(root)
    if 2*i+1 < len(in1):
        if in1[2*i+1] != "null":
            root.left = buildTree(2*i+1)
    if 2*i+2 < len(in1):
        if in1[2*i+2] != "null":
            root.right = buildTree(2*i+2)
    return root
def dfs(root,n):
    if not root.left and not root.right:
        return 1
    k1,k2 = 0,0
    if root.left:
        k1 = dfs(root.left, n)+1
    if root.right:
        k2 = dfs(root.right, n)+1
    return max(k1,k2)
def del_s(s):
    s = s.replace("[","")
    s = s.replace("]","")
    return s

for _ in range(int(input())):
    nodes = set()
    in1 = list(map(str, del_s(input()).split(",")))
    buildTree(0)
    out = 0
    for i in nodes:
        if i.left and i.right:
            out = max(out,dfs(i.left,0)+dfs(i.right,0))
        elif i.left:
            out = max(out, dfs(i.left,0))
        elif i.right:
            out = max(out, dfs(i.right,0))
    print(out)

"""
5
[6,5,7]
[1,2,3,4,5]
[1,2,3,4,6,null,7]
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,null,null,null,null,null,null,15]

4
[6,null,7]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
[1,2,99,null,null,3]
[99,2,3,4,null,6,7,8,null,null,null,12]
"""