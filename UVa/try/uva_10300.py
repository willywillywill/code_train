for _ in range(int(input())):
    lst = []
    ans = 0
    for _ in range(int(input())):
        l = list(map(int,input().split()))
        ans += l[0]/l[1]*l[2]*l[1]
    print(int(ans))

"""
3
5
1 1 1
2 2 2
3 3 3
2 3 4
8 9 2
3
9 1 8
6 12 1
8 1 1
3
10 30 40
9 8 5
100 1000 70
"""