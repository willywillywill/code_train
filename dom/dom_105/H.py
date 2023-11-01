class node:
    def __init__(self,data, s=None, left=None, right=None):
        self.s = s
        self.data = data
        self.left = left
        self.right = right

def dfs(root, lst, lr=None):
    global st
    if root:
        if lr!=None:
            lst.append(lr)
        if root.s:
            lst.append(root.s)
        dfs(root.left, lst.copy(), lr=0)
        dfs(root.right, lst.copy(), lr=1)
    else:
        st.add(tuple(lst))

str_text = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")



for _ in range(int(input())):
    in1 = list(map(int, input().split(",")))
    data = [ [str_text[i],in1[i]] for i in range(len(in1)) ]
    nodes = [ node(i[1],i[0]) for i in data ]
    # bottom-up
    while len(nodes) > 1:
        n = []
        for i in range(2):
            k = [ i.data for i in nodes ]
            idx = k.index(min(k))
            k.pop(idx)
            n.append(nodes.pop(idx))

        root = node(n[0].data + n[1].data)
        root.left = n[0]
        root.right = n[1]
        nodes.append(root)
    root = nodes[0]
    st = set()
    dfs(root,[])
    lst = sorted(list(st), key=lambda x:x[-1])
    out = [ str(len(lst[i][:-1])) for i in range(len(lst)) ]
    print(",".join(out))

"""
2
2,3,6,8,13,15,19
4,8,5

3
26,25,20,15,10,5
4,3,5,6
2,1 
"""