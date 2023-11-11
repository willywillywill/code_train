"""  遞迴函數
w = [10,20,40]
mone = 100

def f(l,m,r):
    if m == 0:
        print(r)
        return 0
    if m <0:
        return
    for i in l:
        if m-i >= 0:
            o = r.copy()
            o.append(i)
            f(l.copy(),m-i,o.copy())
f(w.copy(),mone,[])
"""
w = [10,20,40]
mone = 100
dp = [0]*(mone+1)
dp[0] = 1
for cost in w:
    for i in range(cost,mone+1):
        dp[i] += dp[i-cost]
print(dp)