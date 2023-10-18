class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def dfs(i,n):
    global ans
    k = 1
    if i.left:
        k=0
        dfs(i.left,n+1)
    if i.right:
        k=0
        dfs(i.right,n+1)
    if k:
        ans+=n
n = int(input())
lst = list(map(int,input().split()))
free_nodes = [ node(i) for i in lst ]
while len(free_nodes)!=1:
    node_val = [ i.val for i in free_nodes ]
    idx_min_node1 = node_val.index(min(node_val))
    min_node1 = free_nodes.pop(idx_min_node1)

    node_val = [ i.val for i in free_nodes ]
    idx_min_node2 = node_val.index(min(node_val))
    min_node2 = free_nodes.pop(idx_min_node2)
    n = node(min_node1.val+min_node2.val)
    n.left = min_node2
    n.right = min_node1

    free_nodes.append(n)
tree = free_nodes[0]

ans = 0
dfs(tree,0)
print(ans)
"""
6
26 25 20 15 10 5
"""