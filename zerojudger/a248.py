"""
由於程式裡「小數位數」有上限，
超過上限會以 0 呈現，
因此不能直接用數字相除來求得答案 ( 結果會發生錯誤 )，
所以必須先將數字乘以「10^位數」
"""
while 1:
    try:
        a,b,n = list(map(int,input().split()))
        rd = a*(10**n)//b
        rs = str(rd)
        if len(rs) < n:
            for i in range(n-len(rs)):
                rs = "0"+rs
        m = rs[(n*-1):]
        n = rs[:(n*-1)]
        if n == "":
            n = "0"
        print("%s.%s"%(n,m))
    except:
        break

"""
18467 41 10
26500 6334 10
15724 19169 10
10 5 3
"""