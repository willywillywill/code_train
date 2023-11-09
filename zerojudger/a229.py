def pa(le,ri,n):
    if n==2*num:
        print("".join(qu))
        return
    if le < num:
        qu.append("(")
        pa(le+1, ri, n+1)
        qu.pop(-1)
    if le>ri and ri<num:
        qu.append(")")
        pa(le,ri+1,n+1)
        qu.pop()

import sys
try:
    for i in sys.stdin:
        qu = []
        num = int(i)
        pa(0,0,0)
        print()
except:
    pass