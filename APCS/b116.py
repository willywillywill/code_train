while 1:
    try:
        n,m = map(int,input().split())
        for _ in range(n):
            lst = list(map(int,input().split()))
            s = set()
            s.add(0)
            for i in lst:
                ns = set()
                for j in s:
                    ns.add(j+i)
                    ns.add(j-i)
                s = ns
            if 0 in s:
                print("Yes")
            else:
                print("No")
    except:
        break