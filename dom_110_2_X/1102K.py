c = 0
while 1:
    try:
        if c!=0:
            input()

        x = int(input())
        y = int(input())
        m = int(input())
        print(pow(x,y,m))
        c+=1
    except:
        break

"""
10
2009
9


2374859
3029382
36123
"""