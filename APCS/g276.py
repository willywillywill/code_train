n,m,k = list(map(int,input().split()))
bomb=[[0]*m for _ in range(n)]
save = [1]*k

data = []
for i in range(k):
    data.append([i]+[int(x) for x in input().split()])

while 1 in save:
    rm_bomb = []
    for i,r,c,_,_ in data:
        if save[i]==1:
            bomb[r][c] = 1
    for i,r,c,s,t in data:
        if save[i]==0:
            continue
        nextr,nextc = r+s,c+t
        data[i] = [i,nextr,nextc,s,t]
        if 0<=nextr<n and 0<=nextc<m:
            if bomb[nextr][nextc] == 1:
                save[i] = 0
                rm_bomb.append([nextr,nextc])
        else:
            save[i] = 0
    for x,y in rm_bomb:
        bomb[x][y] = 0
ans = 0
for i in bomb:
    for j in i:
        ans += j
print(bomb)
print(ans)
"""
n,m,k = map(int,input().split())
st = []
save = [1]*k
move = []
bomb = []
for i in range(k):
    r,c,s,t = list(map(int,input().split()))
    st.append([s,t])
    move.append([r,c])
while 1 in save:
    rm_bomb = []
    for i in range(k):
        if save[i]:
            bomb.append(move[i])

    for i in range(k):
        if save[i]==0: continue    
        move[i] = [move[i][0]+st[i][0],move[i][1]+st[i][1]]
        if 0<= move[i][0]<n and 0<=move[i][1]<m:
            if move[i] in bomb:
                save[i] = 0
                rm_bomb.append(move[i])
        else:
            save[i] = 0

    for i in rm_bomb:
        del bomb[bomb.index(i)]
print(bomb)
"""


"""
5 5 2
0 0 3 2
0 0 2 3
"""