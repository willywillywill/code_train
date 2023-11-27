
input()
in1 = list(map(int,input().split()))
c = 0
f = False
lst = [ [0,0] for i in range(9) ] # vis time
while in1:
    u = in1.pop(0)
    for i in lst:
        if i[1] != 0:
            i[1] -= 1
    if u==-1:
        continue
    if lst[u-1][0]==0:
        lst[u-1][0] = 1
        c+= u
    if lst[u-1][1]==0:
        lst[u-1][1] = 12
    
    if 0 not in [ i[1] for i in lst ]:
        f = True
if f:
    print("perfect")
else:
    print(c)

"""
1 2 3 4 5 5
"""