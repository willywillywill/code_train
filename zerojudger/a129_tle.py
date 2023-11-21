

def find_ptr(x):
    if ptr[x] != x:
        return find_ptr(ptr[x])
    return ptr[x]

def v(x, vis_v):
    if vis_v[x] == 3:
        return
    vis_v[x] += 1
    for i in g[x]:
        v(i, vis_v)

while 1:
    try:
        n,m = map(int,input().split())
        lst = []
        ptr = { i:i for i in range(n) }
        vis = { i:0 for i in range(n) }
        g = {}
        for _ in range(m):
            a,b,w = map(int,input().split())
            lst.append([a,b,w]) 
            if a not in g:
                g[a] = []
            if b not in g:
                g[b] = []
            g[a].append(b)
            g[b].append(a)

        for i in g:
            vis_v = { i:0 for i in range(n) }
            v(i, vis_v)
            if 0 in vis_v.values():
                print(-1)
                break
        else:
            val = 0
            lst.sort(key=lambda x:x[-1])
            while lst:
                a,b,w = lst.pop(0)
                pa = find_ptr(a)
                pb = find_ptr(b)
                if pa != pb:
                    ptr[pa] = b
                    val += w
            print(val)
    except:
        break
