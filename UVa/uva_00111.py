n = int(input())
c = list(map(int,input().split()))
c_ = [0]*n
for i in c:
    c_[i-1] = c.index(i)
c = [0]+c_.copy()

while 1:
    try:
        r = list(map(int,input().split()))
        r_ = [0]*n
        for i in r:
            r_[i-1] = r.index(i)
        r = [0]+r_.copy()

        dp = [ [0]*(n+1) for _ in range(n+1) ]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if c[i]==r[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp[-1][-1])
    except:
        break

"""
10
3 1 2 4 9 5 10 6 8 7
1 2 3 4 5 6 7 8 9 10
4 7 2 3 10 6 9 1 5 8
3 1 2 4 9 5 10 6 8 7
2 10 1 3 8 4 9 5 7 6

"""