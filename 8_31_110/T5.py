s = list(map(str, input().split(",")))
sx = len(s)
sy = len(s[0])
qu = [(0,0)]
lst = [ [ 0 for i in range(sy) ] for j in range(sx) ]
move = []
sum_num = 0

for i in range(sx):
    for j in range(sy):
        if s[i][j] != "0":
            lst[i][j] = 1 if lst[i][j]==0 else lst[i][j]
            if 0 <= i+1 < sx:
                if s[i+1][j] != "0" and lst[i+1][j] != lst[i][j]:
                    lst[i+1][j] = lst[i][j]+1
            if 0 <= i-1 < sx:
                if s[i-1][j] != "0" and lst[i-1][j] != lst[i][j]:
                    lst[i-1][j] = lst[i][j]+1
            if 0 <= j+1 < sy:
                if s[i][j+1] != "0" and lst[i][j+1] != lst[i][j]:
                    lst[i][j+1] = lst[i][j]+1
            if 0 <= j-1 < sy:
                if s[i][j-1] != "0" and lst[i][j-1] != lst[i][j]:
                    lst[i][j-1] = lst[i][j]+1

        
print(lst)

"""
02012,01100,20211,00120
"""