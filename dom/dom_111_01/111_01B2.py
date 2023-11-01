
for _ in range(int(input())):
    lst = list(map(int,input().split()))
    if lst[0]==lst[1]==lst[2]==lst[3]:
        print("square")
    elif lst[0]==lst[2] and lst[1]==lst[3]:
        print("rectangle")
    elif sorted(lst)[-1] <= sum(sorted(lst)[:-1]):
        print("quadrangle")
    else:
        print("banana")
"""
8
65535 65535 65535 65535
5647 2948 5647 2948
67 34 90 12
657 354 23 189
546 387 987 234
675 354 987 254
12 45 36 27
78 56 47 39
"""