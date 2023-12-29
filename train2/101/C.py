def Height(x, px):
    h = 1
    for i in tree[x]:
        h = max(h, Height(i, x)+1)
    return h

for _ in range(int(input())):
    if _:
        input()
    m = int(input())
    tree = { i:[] for i in range(21)}
    for i in range(m-1):
        a,b = map(int,input().split(","))
        tree[b].append(a)

    print(Height(0,0))


"""
2 
7 
1,3 
2,3 
3,5 
4,5 
5,0 
6,5

8 
1,6
2,3
3,4
4,6
5,6
6,0
7,2
"""