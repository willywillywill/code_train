n = int(input())
lst = [0]+list(map(int,input().split()))
dit = { i:lst[i] for i in range(len(lst))}
dit[len(dit)] = None

def f(d:dict,pt):
    if dit[pt] == None:
        l = [ dit[i] for i in d ]
        if sum(l):
            ans.add(str(sum(l)))
        return
    
    d[pt] = dit[pt]
    k = 1
    for i in dit:
        if i not in d:
            k = 0
            f(d.copy(),i)    

ans = set()
f({},0)
ans = sorted(list(ans), key=lambda x:int(x))
print(len(ans))
print(" ".join(ans))
"""
4
4 2 2 5
"""