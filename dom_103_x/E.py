# ~ b159
import itertools




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
    in1 = list(map(int,input().split()))
    in1 = itertools.combinations(in1,5)
    out = []
    for in1_ in in1:
        mod_lst = [ (i-1)%13 for i in in1_ ]
        div_lst = [ (i-1)//13 for i in in1_ ]
        mod_lst.sort()
        div_lst.sort()

        g = [mod_lst.count(ii) for ii in range(14)]

        if max(div_lst)==min(div_lst) and n(mod_lst):
            k = 7
        elif max(g)>=4:
            k = 6
        elif 3 in g and 2 in g:
            k = 5
        elif n(mod_lst):
            k = 4
        elif 3 in g:
            k = 3
        elif g.count(2)>=2:
            k = 2
        elif g.count(2):
            k = 1
        else:
            k = 0
        out.append(k)
    print(max(out))    

"""
2 
3 44 4 6 7 5 
19 12 1 32 45 25 

2 
14 16 18 19 20 21 
4 17 30 43 9 22
"""