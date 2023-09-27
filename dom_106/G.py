"""
5
1,2 2,3 4,0
4,3 2,3 2,1 1,0
1,2 2,3 3,4 1,4 1,5
1,2 1,3 2,3
1,2 2,3 3,4 1,5 5,4 

"""

def dfs(x,px,l):
    if x in dit:
        l.append(x)
        for i in dit[x]:
            if px!=i:
                if i in l:
                    lst.append(l)
                    break
                else:
                    dfs(i,x,l.copy())
            else:
                st.append(l)

dit = {}
lst = []
st = []
in1 = list(map(str, input().split()))
in1 = [ list(map(int,i.split(","))) for i in in1 ]
nodes = set()
for i in in1:
    nodes.add(i[0])
    nodes.add(i[1])
    if i[0] in dit:
        dit[i[0]].append(i[1])
    else:
        dit[i[0]] = [i[1]]
    if i[1] in dit:
        dit[i[1]].append(i[0])
    else:
        dit[i[1]] = [i[0]]
nodes = list(nodes)
dfs(nodes[0],nodes[0],[])
l = set()
for i in st:
    for j in i:
        l.add(j)
if lst:
    p = [ str(i) for i in sorted(lst[0]) ]
    print(", ".join(p))
else:
    if len(l) == len(nodes):
        print("T")
    else:
        print("F")



