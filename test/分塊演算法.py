"""
n,m = map(int,input().split())
lst = list(map(int,input().split()))
for _ in range(m):
    dit = {}
    a,b = map(int,input().split())
    a,b = a-1,b-1
    for i in lst[a:b+1]:
        dit[i] = dit.get(i,0)+1
    dit = list(dit.items())
    dit.sort(key=lambda x:x[1],reverse=True)
    mm = dit[0][1]
    ans = 0
    for i in dit:
        if i[1]==mm:
            ans += 1
    print(mm,ans)
"""

def query(l,r):
    ans = 0
    for i in range(l,r+1):
        if i/k != l/k:
            break
        ans =  max(ans,lst[i])
    for i in range(r,l+1,-1):
        if i/k != r/k:
            break
        ans = max(ans,lst[i])
    for i in range(l//k+1, r//k):
        ans = max(ans,block[i])
    return ans

n = int(input())
lst = list(map(int,input().split()))
k = int(n**0.5)
block = [0]*n
for i in range(n):
    block[i//k] = max(block[i//k], lst[i])

for i in range(int(input())):
    l = list(map(int,input().split()))
    print(query(min(l)-1,max(l)-1))



"""
10 
3 2 4 5 6 8 1 2 9 7
7 
1 5 
3 5
1 10
5 8
6 6 
2 4
2 9 
"""