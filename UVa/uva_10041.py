
for _ in range(int(input())):
    lst = list(map(int,input().split()))[1:]
    lst.sort()

    if len(lst)%2:
        m = lst[len(lst)//2]
    else:
        m = lst[len(lst)//2-1:len(lst)//2+1]
        m = sum(m)//2
    num = 0
    for i in lst:
        num += abs(m-i)
    print(num)


"""
3
2 2 4
3 2 4 6
4 2 1 999 5
"""