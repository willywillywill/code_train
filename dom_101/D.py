def dfs(x, px):
    global ans
    for i in range(len(tree)):
        if 1 not in tree[x][:i]+tree[x][i+1:]:
            vv[x]=1
        if tree[x][i] and i!=px:
            v[i] +=1
            if v[i]>1:
                ans = 1
                break
            dfs(i,x)

for _ in range(int(input())):
    in1 = list(map(str, input().split()))
    in1 = [ list(map(int, i.split(","))) for i in in1 if i!="0,0" ]
    if not in1:
        print(0)
        continue
    st = set()
    for i in in1:
        st.add(i[0])
        st.add(i[1])

    tree = [[ 0 for i in range(max(st)+1) ] for j in range(max(st)+1)]

    for i in in1:
        tree[i[0]][i[1]] = 1
        tree[i[1]][i[0]] = 1
        
    v = [0]*len(tree)
    vv = [0]*len(tree)
    ans = 0

    dfs(0,0)
    if ans:
        print("F")
    else:
        print(sum([ i for i in vv if i==1 ])-1)

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