# 8Queen DFS(H)
# https://web.ntnu.edu.tw/~algo/Backtracking.html

def fun(x):
    if x==8:
        ans.add(tuple(g))
        return

    for y in range(8):
        d1 = (x+y)%15
        d2 = (x-y+15)%15
        if  not T_B[y] and not LT_RB[d1] and not RT_LB[d2]:
            T_B[y] = LT_RB[d1] = RT_LB[d2] = 1
            g[x] = y
            fun(x+1)
            T_B[y] = LT_RB[d1] = RT_LB[d2] = 0

for i in range(int(input())):
    val = []
    for i in range(8):
        val.append(list(map(int,input().split())))

    g = [ 0 for i in range(8)]
    LT_RB = [0]*15
    RT_LB = [0]*15
    T_B = [0]*8
    ans = set()
    fun(0)
    max_sum = 0
    for i in ans:
        l = [0]*8
        for j in range(len(i)):
            l[j] = val[j][i[j]]
        max_sum = max(max_sum, sum(l))
    print(max_sum)

"""
 1  2  3  4  5  6  7  8
 9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
48 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64

"""