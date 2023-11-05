for i in range(int(input())):
    lst = list(map(int,input().split()))
    if lst[0] == 1:
        print(lst[1]+lst[2])
    elif lst[0] == 2:
        print(lst[1]-lst[2])
    elif lst[0] == 3:
        print(lst[1]*lst[2])
    else:
        print(lst[1]//lst[2])