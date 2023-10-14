max_val = 10000
dp = [ 0 for _ in range(max_val+1) ]
dp[0] = 1
MOD = 100000
t=1
for i in range(1,max_val+1):
    t *=i
    while t%10==0:
        t /= 10    
    dp[i] = t%10
    t%=MOD


while 1:
    try:
        n = int(input())
        num = int(dp[n])
        print("%4s -> %s"%(n,num))
    except:
        break


