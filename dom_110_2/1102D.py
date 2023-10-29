n = int(input())
lst = list(map(int,input().split()))
lst.sort()

n = 0
while sum(lst) %2 != 0:
    if lst[n]%2 !=0:
        del lst[n]
    n+=1
print(sum(lst))



"""
3
2 2 3
"""