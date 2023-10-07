for _ in range(int(input())):
    lst = list(map(int, input().split()))
    for i in range(2):
        a1 = lst.pop(lst.index(max(lst)))
        print(a1, end=" ")
    print()
"""
3 
1 2 3 4 10 9 8 7 
10 11 12 99 1 2 3 
1 2 1 2 1 2
"""