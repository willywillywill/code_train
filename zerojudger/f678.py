def find_ptr(x):
    if ptr[x] != x:
        return find_ptr(ptr[x])
    return ptr[x]

n,m = map(int,input().split())
lst = []
ptr = {}
num = {}
for _ in range(m):
    u,v,w = map(int,input().split())
    lst.append([u,v,w])
    ptr[u] = u
    ptr[v] = v
lst.sort(key=lambda x:x[2])
val = 0
while lst:
    a,b,w = lst.pop(0)
    pa = find_ptr(a)
    pb = find_ptr(b)
    if pa != pb:
        ptr[pa] = b
        val += w
print(val)