
txt = list("+-*/")
in1,ans = input().split()
ans = int(ans)

def dfs(n):
    if n==0:
        return
    if 