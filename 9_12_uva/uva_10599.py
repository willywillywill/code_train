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

t = []
for i in range(1, len(xy)):
    xy1 = xy[i-1]
    xy2 = xy[i]
    
    lst = [ [0 for i in range(min(xy1[1],xy2[1]),max(xy1[1],xy2[1])+1)] for j in range(min(xy1[0],xy2[0]),max(xy1[0],xy2[0])+1) ]

    for j in range(len(lst)):
        for k in range(len(lst[0])):
            if j==0 or k==0:
                lst[j][k] = 1
            else:
                lst[j][k] = max(lst[j-1][k], lst[j][k-1])+1
    t.append(lst[-1][-1])
print(t)
