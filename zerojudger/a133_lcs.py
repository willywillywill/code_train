k=1
while 1:
    n1,n2 = list(map(int, input().split()))
    if n1==n2==0:
        break
    str1 = list(map(str, input().split()))
    str2 = list(map(str, input().split()))

    lst1 = [[ 0 for i in range(len(str2)) ]for j in range(len(str1))]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                lst1[i][j] = 1 if j-1<0 else lst1[i-1][j-1]+1
            else:
                lst1[i][j] = max(lst1[i][j-1], lst1[i-1][j])

    print("Twin Towers #%d"%(k))
    print("Number of Tiles :",lst1[-1][-1])
    k+=1