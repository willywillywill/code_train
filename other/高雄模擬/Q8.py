# dijkstra (queue-BFS)
val = {}
vis = {}
next_ = {}
start,end=None,None
while 1:
    try:
        a,b,c = input().split()
        if start==None:
            start = a
        end = b
        if a not in next_:
            next_[a] = []
        if b not in next_:
            next_[b] = []
        next_[a].append(b)
        val[a+b] = int(c)
        vis[a] = 0
        vis[b] = 0
    except:
        break

qu = [(start,0,[])]
while qu:
    qu.sort(key=lambda x:x[1])
    n,v,r = qu.pop(0)
    if vis[n]:
        continue
    r.append(n)
    if n==end:
        print("共花了:",v)
        print(" ".join(r))
        break
    vis[n] = 1
    for i in next_[n]:
        qu.append((i,v+val[n+i], r.copy()))

"""
別針 海報 5
別針 門票 30
海報 變形金剛 25
海報 滑板車 80
門票 滑板車 40
門票 變形金剛 35
滑板車 動物森友會 200
變形金剛 動物森友會 275
"""