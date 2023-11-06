
xy1 = list(map(eval,input().split()))
xy2 = list(map(eval,input().split()))
xy3 = list(map(eval,input().split()))
xy4 = list(map(eval,input().split()))

h = (xy1[0]**2-xy2[0]**2)*(xy1[1]-xy3[1])-(xy1[0]**2-xy3[0]**2)*(xy1[1]-xy2[1]) \
            /(2*((xy1[0]-xy2[0])*(xy1[1]-xy3[1])-(xy1[0]-xy3[0])*(xy1[1]-xy2[1])))
print(h)

"""
3 0
-1 0
1 2
2.5 1.5
"""