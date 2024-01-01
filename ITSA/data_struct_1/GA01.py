# kir... 
def find(x):
    if  ptr[x] != x:
        ptr[x] = find(ptr[x])
    return ptr[x]

n,m = map(int,input().split())
lst = input().split()
arr = []
ptr = { i:i for i in lst }
for i in range(m):
    a,b,v = input().split()
    arr.append([a,b,int(v)])
arr.sort(key=lambda x:x[-1])
ans = []
count = 0
for a,b,v in arr:
    la = find(a)
    lb = find(b)
    if la != lb:
        ptr[lb] = la
        ans.append((int(a[1:]),int(b[1:])))
        count += v
ans.sort(key=lambda x:(x[0],x[1]))
for a,b in ans:
    print(f"(W{a} W{b})",end="")
print()
print(count)
"""
7 11
W1 W2 W3 W4 W5 W6 W7
W1 W2 1
W1 W4 4
W2 W3 2
W2 W4 6
W2 W5 4
W3 W5 5
W3 W6 6
W4 W5 3
W4 W7 4
W5 W6 8
W6 W7 3
"""