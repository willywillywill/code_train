while 1:
    try:
        w = []
        v = []
        n = int(input())
        for _ in range(n):
            a,b = map(int,input().split())
            w.append(a)
            v.append(b)
        dp = [ [0]*101 for i in range(len(w)+1) ]
        for i in range(n):
            for j in range(0,101):
                if j-w[i] < 0:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])
        print(dp[-1][-1])
    except:
        break