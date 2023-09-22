
def dfs(x,px):
    global v
    for i in dit:
        if val[i] > 1:
            v=1
            break
        if len(dit[x][:i]+dit[x][i+1:])==0:
            vv[x] = 1
        if i in dit[x] and px != i:
            val[i] += 1
            dfs(i,x)

for _ in range(int(input())):
    in1 = list(map(str, input().split()))
    lst = []
    c=0
    for i in range(len(in1)):
        k = list(map(int, in1[i].split(",")))
        if k[0] != k[1] or k[0]==k[1]==0:
            lst.append(k)
        else:
            c=1

    if c:
        print("F")
        continue
    if len(lst)==1:
        print(0)
        continue

    dit = {}
    for i in lst:
        if i[0] in dit:
            dit[i[0]].append(i[1])
        else:
            dit[i[0]] = [i[1]]
        if i[1] in dit:
            dit[i[1]].append(i[0])
        else:
            dit[i[1]] = [i[0]]

    val = [0]*(max(dit)+1)
    v = 0
    vv = [0]*(max(dit)+1)
    dfs(0,0)

    if v:
        print("F")
        continue

    k = 0
    for i in dit:
        if val[i] == 0 and i != 0:
            print("F")
            k=1
            break
    if k:
        continue
        
    print(sum([ i for i in vv if i==1]))

"""

5
6,8 5,3 5,2 6,4 5,6 1,2 2,0 0,0
8,1 1,3 6,2 8,10 7,5 1,4 7,8 7,6 8,0 0,0
3,8 6,8 6,4 5,3 5,6 8,2 2,0 0,0
0,0
1,0 0,0

4
4,3 2,3 2,1 1,0 0,0
1,1 0,0
1,2 2,3 4,0 0,0
1,2 2,3 3,1 4,5 5,0 0,0
"""