
class Graph:
    def __init__(self, node_number, edge_number):
        self.adj = [[] for i in range(node_number)]
        self.color = [0]*node_number
        for i in range(edge_number):
            a,b = map(int,input().split())
            self.adj[a].append(b)
            self.adj[b].append(a)
def f(graph, root):
    l = []
    for i in graph.adj[root]:
        l.append(graph.color[i])
    c = 1
    while c in l:        
        c += 1
    graph.color[root] = c
    return c

node_num = int(input())
edge_num = int(input())
graph = Graph(node_num, edge_num)


"""
4
3
0 2
2 3
3 1
"""