
lst = [ list(map(int, input().split())) for i in range(9) ]

def l1(xy1): # row & clo
    l = [ lst[xy1[0]][::], 
                [ lst[i][xy1[1]] for i in range(len(lst)) ] ]
    del l[0][xy1[0]]
    del l[1][xy1[1]]
    if (lst[xy1[0]][xy1[1]] in l[0]) and (lst[xy1[0]][xy1[1]] != 0):
        return 1
    return tuple(l[0]),tuple(l[1])

def l2(xy1): # box
    l = []
    xy2 = [xy1[0]+3, xy1[1]+3]
    for i in range(xy1[0],xy2[0]):
        for j in range(xy1[1], xy2[1]):
            if (lst[i][j] in l) and (lst[i][j] != 0):
                return 1
            l.append(lst[i][j])
    return tuple(l)




    
"""
0 0 3 9 0 0 7 6 0
0 4 0 0 0 6 0 0 9
6 0 7 0 1 0 0 0 4
2 0 0 6 7 0 0 9 0
0 0 4 3 0 5 6 0 0
0 1 0 0 4 9 0 0 7
7 0 0 0 9 0 2 0 1
3 0 0 2 0 0 0 4 0
0 2 9 0 0 8 5 0 0
"""