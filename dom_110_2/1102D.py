n = int(input())
lst = list(map(int,input().split()))
if sum(lst)%2==0:
    print(sum(lst))
else:
    for i in range(len(lst)):
        if lst[i]%2 != 0:
            del lst[i]
            break
    print(sum(lst))

"""
3
1 2 3
"""