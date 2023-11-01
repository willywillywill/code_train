"""
2
12/11/2020
01/01/2019
30/11/2020
01/12/2019
"""
for _ in range(int(input())):
    lst2 = list(map(int,input().split("/")))
    lst1 = list(map(int,input().split("/")))
    y = lst2[2]-lst1[2]
    if lst2[1]<lst1[1]:
        y-=1
    elif lst2[1] == lst1[1] and lst2[0] < lst1[0]:
        y-=1
    
    print(y)