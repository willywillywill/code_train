class node:
    def __init__(self,val):
        self.val = int(val)
        self.left = None
        self.right = None
def dfs(i,l):
    k=1
    if i.left:
        k=0
        l.append(i.val)
        dfs(i.left,l.copy())
    if i.right:
        k=0
        l.append(i.val)
        dfs(i.right,l.copy())
    if k:
        ans.add(tuple(l))


n = 7
free_nodes = list(map(node,"2 3 6 8 13 15 19".split()))
while len(free_nodes)!=1:
    val = [ i.val for i in free_nodes ]
    node1 = free_nodes.pop(val.index(min(val)))
    val = [ i.val for i in free_nodes ]
    node2 = free_nodes.pop(val.index(min(val)))
    new_node = node(node1.val+node2.val)
    new_node.left = node2
    new_node.right = node1
    free_nodes.append(new_node)

ans = set()
dfs(free_nodes[0], [])
print(ans)
"""
7
2 3 6 8 13 15 19
"""