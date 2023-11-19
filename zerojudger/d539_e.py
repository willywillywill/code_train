n = int(input())
def build(L=0,R=n-1,idx=0):
    print(L,R)
    if L==R:
        mx[idx] = lst[L]
        return
    mx[idx] = max(lst[L:R+1])
    m = (L+R)//2
    build(L,m,2*idx+1)
    build(m+1,R,2*idx+2)
    
def query(l,r,L,R,idx):
    if l<=L and R<=r:
        return mx[idx]
    m = (L+R)//2
    if r<=m:
        return query(l,r,L,m,2*idx+1)
    elif l>m:
        return query(l,r,m+1,r,2*idx+2)
    else:
        return max(query(l,r,L,m,2*idx+1),query(l,r,m+1,R,2*idx+2))



lst = list(map(int,input().split()))
mx = [0]*1000000
build()
print(mx[:20])
for _ in range(int(input())):
    l,r = map(int,input().split())
    if l > r:
        r,l = l,r
    if l==r:
        print(lst[l-1])
    else:
        print(query(l-1,r-1,0,n-1,0))
