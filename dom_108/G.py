# !!!  https://www.techiedelight.com/zh-tw/greedy-coloring-graph/

class Graph:
    def __init__(self, edges, n):
        self.adjList = [ [] for _ in range(n) ]
        
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def colorGraph(graph, n):
    result = {}
    for u in range(n):
        assigned = set([ result.get(i) for i in graph.adjList[u] if i in result ])
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color+1
        print(color)
        result[u] = color
        print(result)
    return result


node_number = int(input())
edge_number = int(input())
edges = []
for i in range(edge_number):
    edges.append(tuple(map(int,input().split())))
graph = Graph(edges, node_number)
result = colorGraph(graph, node_number)


"""
color_number = len(set(result.values()))
if color_number >2:
    print("F")
else:
    print("T")
"""

"""
2
4
4
0 1
1 2
2 3
3 0
5
10
0 1
0 2
0 3
0 4
1 2
1 3
1 4
2 3
2 4
3 4
"""