def dfs(i,l):
    global ans
    l.append(i)
    k = []
    if i in tree:
        for j in tree[i]:
            if j not in l:
                dfs(j,l.copy())
                k.append(j)
    if not k:
        ans.append(l[1:])
t = 1
while 1:
    try:
        tree = {}
        for i in range(int(input("輸出範例%d：\n"%(t)))-1):
            a,b = list(map(int,input().split()))
            if a in tree:
                tree[a].append(b)
            else:
                tree[a] = [b]
            if b in tree:
                tree[b].append(a)
            else:
                tree[b] = [a]

        l = [0]*(len(tree)+1)
        ll = [0]*(len(tree)+1)
        for i in tree:
            ans = []
            dfs(i,[])
            for j in ans:
                for k in j:
                    l[k] +=1
                    ll[i] += 1
        out = [0]*(len(tree)+1)
        for i in range(1,len(out)):
            out[i] = l[i]-ll[i]
        print("輸出範例%d："%(t))
        print(out.index(max(out)),max(out)+1)
        t+=1
    except:
        break
"""
8
1 3
3 4
5 4
6 5
8 4
5 7
2 3

6
1 5
2 5
5 4
4 6
3 4
"""