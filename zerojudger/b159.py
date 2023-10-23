def n(l):
    l = [ i for i in l ]
    a = l.pop(0)
    if not l:
        return True
    if a+1 == l[0]:
        return n(l.copy())
    else:
        return False
for _ in range(int(input())):
    lst = [[ 0 for i in range(1,14)] for j in range(4)]
    in1 = list(map(int,input().split()))

    mod_lst = [ (i-1)%13 for i in in1 ]
    div_lst = [ (i-1)//13 for i in in1]
    mod_lst.sort()
    div_lst.sort()

    g = [mod_lst.count(ii) for ii in range(14)]

    if max(div_lst)==min(div_lst) and n(mod_lst):
        print(7)
    elif max(g)>=4:
        print(6)
    elif 3 in g and 2 in g:
        print(5)
    elif n(mod_lst):
        print(4)
    elif 3 in g:
        print(3)
    elif g.count(2)>=2:
        print(2)
    elif g.count(2):
        print(1)
    else:
        print(0)


"""
14 21 22 23 24
"""