# recursion DFS(H)

m,n = list(map(int,input().split()))
lst = []
xy = []
for i in range(n):
    l = list(input())
    for j in range(len(l)):
        if l[j] == ".":
            l[j]=0
        if l[j] == "@":
            l[j]=0
            xy = [i,j]
    lst.append(l)
mxy = [(0,-1),(-1,0),(1,0),(0,1)]

visited = [[ 0 for i in range(m)] for j in range(n)]
def search(i,j):
    global ans
    if 0<=i<n and 0<=j<m:
        if lst[i][j] == 0 and visited[i][j]==0:
            ans+=1
            visited[i][j] = 1
            for mx,my in mxy:
                search(i+mx,j+my)
ans = 0
search(xy[0],xy[1])
print(ans)



"""
6 9
....#.
.....#
......
......
......
......
......
#@...#
.#..#.
"""