m,n=map(int,input().split())
L=[]
Ln=[]
for _ in range(m):
    L.append([int(x) for x in input().split()])
for i in range(m):
    Ln.append(L[i].copy())
i=0
while i<m:
    j=0
    while j<n:
        if L[i][j]==1:
            re=j
            if j==n-1:
                break
            else:
                j+=1
                while L[i][j]!=1 and j!=n-1:
                    j+=1
                if L[i][j]==1:
                    for u in range(re+1,j):
                        Ln[i][u]=1
        j+=1
    i+=1
for i in Ln:
    print(*i)
"""
n,m = map(int,input().split())
lst = []
g = [ [0]*m for i in range(n) ]
v = [ [0]*m for i in range(n) ]

for _ in range(n):
    lst.append(list(map(int,input().split())))

for i in range(n):
    st = []
    l = lst[i].copy()
    while 1 in l:
        idx = l.index(1)
        l[idx] = 0
        if v[i][idx]==0:
            st.append(idx)
        if len(st)==2:
            for j in range(st[0], st[1]+1):
                g[i][j] = 1
            st = []
    while st:
        g[i][st.pop()] = 1

for i in range(m):
    st = []
    l = [ lt[i] for lt in lst ]
    while 1 in l:
        idx = l.index(1)
        if v[idx][i]==0:
            st.append(idx)
        l[idx] = 0
        if len(st)==2:
            for j in range(st[0], st[1]+1):
                g[j][i] = 1
            st = []
    while st:
        g[st.pop(0)][i] = 1
    
for i in g:
    print(*i)
"""
"""
3 5
0 1 0 1 0
0 0 0 0 0
0 1 0 1 0
"""