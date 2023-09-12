n = 5

f = [
    [1,5,2,1,7],
    [1,3,5,7,9],
    [7,8,9,1,2],
    [1,8,9,1,2],
    [5,6,4,9,3]
]
dp = [ [0 for i in range(n)] for j in range(n) ]
queue = [(0,0)]
move = [(1,0),(0,1),(-1,0),(0,-1)]
while queue:
    xy = queue.pop(0)
    dp[xy[0]][xy[1]] = f[xy[0]][xy[1]]
    for i,j in move:
        if 0 <= xy[0]+i < n and dp[xy[0]+i][xy[1]]==0:
            queue.append((xy[0]+i,xy[1]))
        if 0 <= xy[1]+j < n and dp[xy[0]][xy[1]+j]==0:
            queue.append((xy[0],xy[1]+j))
print(dp)
    
    