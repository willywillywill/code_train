

def update(n):
    while n<=len(bit):
        bit[n]+=1
        n+=  n&-n
def query(n): # bit[i-n] > bit[i] -> sum bit[a,b...]
    s = 0
    while n>0:
        s += bit[n]
        n -= n&-n
    return s

max_n,n = list(map(int,input().split()))
arr = list(range(1,max_n+1))

for _ in range(n):
    a1,a2 = list(map(int,input().split()))
    arr[a1-1],arr[a2-1] = arr[a2-1],arr[a1-1]
    ans = 0
    bit = [0]*(10**7)
    for i in range(max_n):
        ans += i-query(arr[i])
        update(arr[i])
    print(ans)
