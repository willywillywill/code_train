
for _ in range(int(input())):
    n,m = map(int,input().split())
    w_lst = list(map(int,input().split()))
    m_lst = list(map(int,input().split()))
    m_we = sum(w_lst)
    dp = [0]*(m_we+1)
    dp[0] = 1

    for w in w_lst:
        for i in range(w,m_we+1):
            dp[i] += dp[i-w]

    s = 0
    for i in m_lst:
        if i <= m_we and dp[i]:
            s += 1
    print(s)

"""
2
2 5
3 5
1 5 2 7 8
3 5
2 5 2
20 1 2 4 9

2 3
2 5
12 20 21
"""