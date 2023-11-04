while 1:
    val,k1,k2,k3 = list(map(int,input().split()))
    if val==k1==k2==k3:
        break
    ans = 0
    ans += 720
    ans += ((val-k1+40)%40)*9
    ans += 360
    ans += ((k2-k1+40)%40)*9
    ans += ((k2-k3+40)%40)*9
    print(ans)