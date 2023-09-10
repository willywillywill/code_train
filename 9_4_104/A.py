
for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split(",")))
    num = 0
    k = lst[0]
    while lst:
        a = lst.pop(0)
        if a>k:
            num += (a-k)*20
        elif a<k:
            num += (k-a)*10
        k = a
    print(num)
