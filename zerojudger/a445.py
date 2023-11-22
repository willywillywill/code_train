
def find_ptr(x):
    if ptr[x] != x:
        ptr[x] = find_ptr(ptr[x])
        return ptr[x]
    return ptr[x]

n,r,q = map(int,input().split())
ptr = { i:i for i in range(1,n+1) }

for i in range(r):
    a,b = map(int,input().split())
    if a==b:
        continue
    a = find_ptr(a)
    b = find_ptr(b)
    ptr[b] = a

for i in range(q):
    a,b = map(int,input().split())
    if find_ptr(a) == find_ptr(b):
        print(":)")
    else:
        print(":(")


"""
4 3 1
1 2
2 4
3 3
1 3

6 5 2
1 2
2 3
5 6
4 5
6 3
"""