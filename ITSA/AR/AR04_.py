
for _ in range(int(input())):
    if _:
        print()
    n,m = map(int,input().split())
    arr = []
    ans = []
    for i in range(n):
        arr.append(list(map(int,input().split())))

    # left - right
    for i in range(n):
        l = []
        t = 1
        for j in range(m):
            if arr[i][j] and t:
                l.append("0")
                t = 0
            else:
                l.append("_")
        t = 1
        for j in range(m-1, -1, -1):
            if arr[i][j] and t:
                l[j] = "0"
                t = 0
        ans.append(l)
    # top - down
    for j in range(m):
        t = 1
        for i in range(n):
            if arr[i][j] and t:
                ans[i][j] = "0"
                t = 0
        t = 1
        for i in range(n-1, -1, -1):
            if arr[i][j] and t:
                ans[i][j] = "0"
                t = 0
    for i in ans:
        print(*i)

"""
_ _ _ _ _ _ _
_ _ 0 0 0 _ _
_ 0 _ _ _ 0 _
_ _ 0 0 0 _ _
_ _ _ _ _ _ _

_ _ _ _ _ _ _ _ _ _ _
_ _ 0 0 _ _ _ 0 0 _ _
_ 0 _ _ 0 _ 0 _ _ 0 _
_ _ 0 _ _ 0 _ _ 0 _ _
_ _ _ 0 _ _ _ 0 _ _ _
_ _ _ _ 0 _ 0 _ _ _ _
_ _ _ _ _ 0 _ _ _ _ _
_ _ _ _ _ _ _ _ _ _ _


"""