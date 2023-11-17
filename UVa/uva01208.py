class edge:
    def __init__(self, s, f, w):
        self.s = s
        self.f = f
        self.w = w

def find(i):
    if parent[i] != i:
        return find(parent[i])
    return parent[i]

for _ in range(int(input())):
    e = []
    n = int(input())
    for i in range(n):
        l = list(map(int,input().split(",")))
        for j in range(n):
            if l[j]:
                e.append(edge(i,j,l[j]))
    e.sort(key=lambda x:x.w)
    parent = [ i for i in range(n)]

    print(f"Case {_+1}:")
    for e_ in e:
        ps = find(e_.s)
        pf = find(e_.f)
        if ps != pf:
            print(f"{chr(e_.s+65)}-{chr(e_.f+65)} {e_.w}")  # e_.s e_.f !!
            parent[ps] = pf

"""
1
10
0, 28, 20, 27, 20, 22, 3, 22, 2, 18
28, 0, 27, 19, 1, 1, 18, 24, 12, 11
20, 27, 0, 6, 22, 21, 0, 10, 13, 10
27, 19, 6, 0, 23, 10, 20, 12, 1, 6
20, 1, 22, 23, 0, 21, 9, 29, 3, 20
22, 1, 21, 10, 21, 0, 24, 27, 2, 4
3, 18, 0, 20, 9, 24, 0, 29, 1, 29
22, 24, 10, 12, 29, 27, 29, 0, 26, 9
2, 12, 13, 1, 3, 2, 1, 26, 0, 4
18, 11, 10, 6, 20, 4, 29, 9, 4, 0

"""