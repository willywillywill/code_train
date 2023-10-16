# !

class node:
    def __init__(self,val):
        self.val = int(val)
        self.left = None
        self.right = None
def dfs(i,n):
    k=1
    if i.left:
        k=0
        dfs(i.left,n+1)
    if i.right:
        k=0
        dfs(i.right,n+1)
    if k:
        ans.append(n)

n = 6
free_nodes = list(map(node,"26 25 20 15 10 5".split()))
while len(free_nodes)!=1:
    val = [ i.val for i in free_nodes ]
    node1 = free_nodes.pop(val.index(min(val)))
    val = [ i.val for i in free_nodes ]
    node2 = free_nodes.pop(val.index(min(val)))
    new_node = node(node1.val+node2.val)
    new_node.left = node2
    new_node.right = node1
    free_nodes.append(new_node)

ans = []
dfs(free_nodes[0], 0)
print(sum(ans))

"""
7
2 3 6 8 13 15 19
"""