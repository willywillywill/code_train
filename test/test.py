for _ in range(int(input())):
    input()
    s = sorted(list(map(int,input().split())),reverse=True)
    mid = len(s)//2
    ans = sum(s[:mid])

    for i in range(mid, len(s)):
        ans += s[i]//2
    print(ans)