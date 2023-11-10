# dfs
dit = {}
for i in range(int(input())):
    name,start,end,val = input().split()
    dit[name] = [int(start)//100-7,int(end)//100-7,int(val)]

def dfs(st,en,l):
    global ans   
    s = 0
    for i in l:
        s += dit[i][2]
    if s > ans[0]:
        ans = [s, l]

    for i in range(st,en):
        time[i] = 1

    for i in dit:
        start = dit[i][0]
        end = dit[i][1]
        if 1 not in time[start:end+1]:
            k = l.copy()
            k.append(i)
            dfs(start,end,k.copy())

    for i in range(st,en):
        time[i] = 0

time = [0]*(17-7)
ans = [0,0]
dfs(0,0,[])
print(*ans[1],ans[0])


"""
6
A1 0700 0800 1
A2 0800 1000 6
A3 0800 0900 5
A4 0900 1200 6
A5 1000 1600 12
A6 1300 1700 8
"""