n,s = list(map(int,input().split()))
lst = []
for _ in range(n):
    cp,iv = list(map(int,input().split()))
    add = 0
    if iv < 30:
        add += 10
    elif iv < 40:
        add += 50
    else:
        add += 100
    cp+= (s//1000)*add
    lst.append([_+1,cp])

lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][0],lst[0][1])


"""
3 1000
1520 43
1300 33
1600 22

4 55555
200 42
400 40
500 30
3000 27

3 100
1520 10
1300 10
1600 10
"""