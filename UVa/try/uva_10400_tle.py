
OP = ["+","-","*","/"]
MAX = 32000
MIN = -32000
def judge(s):
    return s>MAX or s<MIN
def dfs(i,val):
    global out,flag
    if flag:
        return
    if i==len(num)-1:
        if val == ans:
            out.append([ OP[j-1] for j in vis ])
            flag = True
        return
    for j in range(len(OP)):
        s = eval("%s%s%s"%(val,OP[j],num[i+1]))
        if judge(s) or \
            (OP[j] == "/" and val % num[i+1] != 0):
            continue
        vis[i] = j+1
        dfs(i+1, s)
        vis[i] = 0
        if flag:
            return

for _ in range(int(input())):
    lst = list(map(int,input().split()))
    num = lst[1:-1]
    ans = lst[-1]
    vis = [0]*(len(num)-1)
    out = []
    flag = False
    dfs(0,num[0])
    if not out:
        print("NO EXPRESSION")
        continue

    out = out[0]
    for i in range(len(num)+len(out)):
        if i%2==0:
            print(num.pop(0),end="")
        else:
            print(out.pop(0),end="")
    print("=%d"%(ans))
