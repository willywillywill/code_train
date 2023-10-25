n = int(input())
lst = list(map(int,input().split()))

if sum(lst)%2==0:
    print(sum(lst))
else:
    while sum(lst)%2!=0:
        for i in range(len(lst)):
            del lst[i]
            break
    print(sum(lst))

"""
5
99999999 99999999 99999999 99999999 99999999
"""