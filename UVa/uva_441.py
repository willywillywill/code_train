from itertools import combinations

n = 0
while 1:
    lst = list(map(int,input().split()))[1:]
    if lst == []:
        break
    elif n:
        print()
    n+=1
    it = list(combinations(lst, 6))
    for i in it:
        print(*i)



