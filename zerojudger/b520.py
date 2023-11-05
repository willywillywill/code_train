for _ in range(int(input())):
    ans = list(map(int,input().split(",")))
    use = list(map(int,input().split(",")))
    ans.sort()
    use.sort()
    count = 0
    for i in range(len(ans)):
        for j in range(len(use)):
            if ans[i]==use[j]:
                count += 1
    print(count)
"""
01, 07, 28, 29, 30
01,07  , 29, 30, 36
"""