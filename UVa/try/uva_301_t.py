"""
https://blog.csdn.net/hyczms/article/details/38546183
10 3 4
0 2 1
1 3 5
1 2 7
2 3 10
10 5 4
2 5 10
2 4 9
0 2 5
2 5 8
0 0 0
"""



class order:
    def __init__(self,fo,to,p):
        self.fo = fo
        self.to = to
        self.passanger = p

def judge(od):
    for i in range(g[od].fo,g[od].to):
        if now[i]+g[od].passanger > lst[0]:
            return 0
    return 1

def dfs(od, count):
    global max_sum
    if count > max_sum:
        max_sum = count
    if od >= lst[2]:
        return
    if judge(od):
        for i in range(g[od].fo,g[od].to):
            now[i] += g[od].passanger
        temp = count + (g[od].to-g[od].fo)*g[od].passanger
        dfs(od+1,temp)
        for i in range(g[od].fo,g[od].to):
            now[i] -= g[od].passanger
    dfs(od+1,count)

lst = list(map(int,input().split()))
g = []
max_sum = 0
ans = []
n = 0
while 1:
    l = list(map(int,input().split()))
    if l[0]==l[1]==l[2]==0:
        break
    g.append(order(l[0],l[1],l[2]))
now = [0]*len(g)
dfs(0,0)
print(max_sum)
print(ans)