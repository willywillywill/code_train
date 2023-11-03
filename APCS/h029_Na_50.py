def to(v,r):
    if r not in tree:
        ans.append(r)
        return
    left = tree[r][0]
    right = tree[r][1]
    if val[left] <= val[right]:
        val[left] += v
        to(v, left)
    else:
        val[right] += v
        to(v, right)
        
def init_val(r):
    if r not in tree:
        return val[r]
    left = init_val(tree[r][0])
    right = init_val(tree[r][1])
    val[r] = left+right
    return left+right

n,m = list(map(int,input().split()))
init_w = list(map(int,input().split()))
w = list(map(int,input().split()))
root = 1
tree = {}
val = {}
for _ in range(n-1):
    p,s,t = list(map(int,input().split()))
    tree[p] = [s,t]
    val[p] = val[s] = val[t] = 0

for i in range(n,2*n):
    val[i] = init_w[i-n]
init_val(root)

ans = []
for i in w:
    to(i,root)
print(*ans)



"""
7 2
9 2 1 6 8 7 5
2 3
1 2 5
2 3 7
3 13 10
4 11 9
6 12 8
5 6 4
"""