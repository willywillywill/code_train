for _ in range(int(input())):

    in1 = list(map(int, input().split()))
    print((in1[0]**in1[1]) % in1[2])

"""
2
10 2009 9
2 99 5

3
3 18132 17
17 1765 3
65535 65535 36123
"""