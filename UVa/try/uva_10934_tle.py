maxk = 100
maxa = 63

f = [[0 for i in range(maxa+1)]for j in range(maxk+1)]
for i in range(1,maxk+1):
    for j in range(1,maxa+1):
        f[i][j] = f[i-1][j-1]+1+f[i][j-1]
def split2Idx(lst,n): # 二分搜尋
    lst = [ [i[0],i[1]] for i in enumerate(lst) ]
    while len(lst) > 1:
        a1 = lst[:len(lst)//2]
        a2 = lst[len(lst)//2:]
        if a1[-1][1] >= n:
            lst = a1
        else:
            lst = a2

    return lst[0]

while 1:
    k,n = list(map(int,input().split()))
    if k==0:
        break

    lst = split2Idx(f[k],n)

    if lst[1] < n:
        print("More than 63 trials needed.")
    else:
        print(lst[0])
