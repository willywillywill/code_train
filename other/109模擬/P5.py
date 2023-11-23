for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())

    if x1==x2 and y1==y2:
        print(0)
    elif x1==x2 or y1==y2:
        print(1)
    elif (y2-y1)/(x2-x1) == 1 or (y2-y1)/(x2-x1) == -1:
        print(1)
    else:
        print(2)

"""
7 
1 8 8 8 
1 5 6 1 
3 7 2 8 
5 5 8 8 
8 3 8 3 
8 3 6 1 
1 3 3 1
"""