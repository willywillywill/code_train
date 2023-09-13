import pprint

x,y = list(map(int, input().split()))
xy = [[0,0]]
"""
6 7
1 2
1 4
2 4
2 6
4 4
4 7
6 6
0 0
"""

while 1:
    s1, s2 = list(map(int, input().split()))
    if s1==s2==0:
        break

    xy.append([s1,s2])

for ii in range(1,len(xy)):
    xy1 = xy[ii-1]
    xy2 = xy[ii]
    print(xy1,xy2)
    
    mx = len(range(xy1[0], xy2[0]))+1
    my = len(range(xy1[1], xy2[1]))+1
    m = [ [ 0 for j in range(my) ] for i in range(mx) ]

    pprint.pprint(m)


"""
for i in range(x):
    for j in range(y):
        if i==j==0:
            m[i][j] = 1
        else:
            if 0 <= i-1 < x:
                m[i][j] = m[i-1][j]+1
            if 0 <= j-1 < y:
                m[i][j] = m[i][j-1]+1


pprint.pprint(m)
"""