
for _ in range(int(input())):
    n = int(input())
    lst = []
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    if sum(lst)==n:
        print("perfect")
    elif sum(lst) < n:
        print("deficient")
    else:
        print("abundant")