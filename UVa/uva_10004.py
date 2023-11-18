
class Graph:
    def __init__(self, node_number, edge_number):
        self.adj = [[] for i in range(node_number)]
        self.node = []
        self.color = [0]*node_number
        for i in range(edge_number):
            a,b = map(int,input().split())
            self.adj[a].append(b)
            self.adj[b].append(a)
            if a not in self.node:
                self.node.append(a)
            if b not in self.node:
                self.node.append(b)
def f(root):
    l = []
    for i in graph.adj[root]:
        l.append(graph.color[i])
    c = 1
    while c in l:        
        c += 1
    graph.color[root] = c
    return c

while 1:
    node_num = int(input())
    if node_num == 0:
        break
    edge_num = int(input())
    graph = Graph(node_num, edge_num)
    c = {}
    for root in graph.node:
        c[root] = f(root)

    if len(set(c.values()))==2:
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")


"""
4
3
0 2
2 3
3 1
"""