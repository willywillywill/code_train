

def dfs(root,l): 
    global ans

    if root not in [99]:
        l.append(root)

    if len(l)-1 == k:
        ans += 1
        return
    
    if root in dit:
        for i in dit[root]:
            dfs(i,l.copy())


for _ in range(int(input())):
    if _:
        input()
    m,k = list(map(int,input().split(",")))
    dit = {}   
    for _ in range(m):
        i,j = list(map(int,input().split(",")))
        if j not in dit:
            dit[j] = []
        dit[j].append(i)
    ans = 0
    dfs(99, [])
    print(ans)

    


"""
3
7,3
0,99
1,3
2,3
3,5
4,5
5,0
6,4

8,2
0,99
1,6
2,5
3,6
4,3
5,6
6,0
7,6

4,3
0,2
1,99
2,3
3,1
"""