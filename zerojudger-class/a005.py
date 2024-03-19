# 1
for _ in range(int(input())):
    lst = list(map(int,input().split()))
    d = ((lst[1]-lst[0]) == (lst[3]-lst[2])) * (lst[1]-lst[0])
    r = ((lst[1]/lst[0]) == (lst[3]/lst[2])) * int(lst[1]/lst[0])
    print(*lst, r*lst[-1] if r else d+lst[-1] )
# 2
for _ in range(int(input())):
    lst = list(map(int,input().split()))
    print(*lst, end=" ")
    if lst[1]-lst[0] == lst[3]-lst[2]:
        print(lst[-1]+(lst[1]-lst[0]))
    else:
        print(lst[-1]*(lst[1]/lst[0]))
