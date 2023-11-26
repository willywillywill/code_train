for _ in range(int(input())):
    ans = False
    lst = list(map(list,input().split()))

    for i in range(len(lst)):
        l = lst.copy()
        for j in range(1,len(l[i])):
            for m in range(0,9):
                k = l[i][j]
                l[i][j] = str(m)
                if l != sorted(l):
                    ans = True
                    break
                l[i][j] = k
            if ans:
                break
        if ans:
            break
    if ans:
        print("Yes")
    else:
        print("No")

"""
3
2020 2020 2020
1 9999999
1 42 4711 9876
"""