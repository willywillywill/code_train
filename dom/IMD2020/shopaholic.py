for _ in range(int(input())):
    input()
    lst = list(map(int,input().split()))
    lst.sort()
    ans = 0
    while len(lst)//3:
        l = [ lst.pop(-1) for _ in range(3) ]
        ans += min(l)
    print(ans)