n = int(input())

dit = {}

def f(l,n=1):
    if len(l)==1:
        return n
    if l[0][1] == l[1][1]:
        del l[0]
        return f(l,n+1)
    return n

for i in range(n):
    dit[i] = []
    for j in range(10):
        url, val = list(map(str, input().split()))
        dit[i].append([url, int(val)])


for i in dit:
    dit[i].sort(key=lambda x:x[1], reverse=True)
    d = dit[i].copy()
    m = f(dit[i])

    print("Case #%s:"%(i+1))
    for j in range(m):
        print(d[j][0])



    
    

