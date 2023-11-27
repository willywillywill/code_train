for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    s1 = list(set(s))
    cnt_s1 = [ s.count(i) for i in s1 ]
    for i in range(k):
        mx = max(cnt_s1)
        idx = cnt_s1.index(mx)
        cnt_s1[idx] -= 1
    print(max(cnt_s1))