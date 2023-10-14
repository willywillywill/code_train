# !!!


def f(n,l=[]):
    for i in range(2, n+1): #判斷質數
        if n%i==0:
            n = n//i
            if i not in l:  
                l.append(i) # 新增因數
            return f(n,l)   # 遞迴到 n 不是質數
    return l

k = 0
while 1:
    a = int(input())
    if a==0:
        break
    l = f(a)
    
    k = len(l)
    print(a,":",k)
    del l[0:k]


    
    
