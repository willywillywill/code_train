# !!!

def f(n):
    k=0  #存找到的因數
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            k=i
            break
    if k!=0:
        l.append(k)
        f(n//k)
    else:
        l.append(n)

while 1:
    a = int(input())
    if a==0:
        break
    if a==1:
        print(a,":",0)
    else:
        l = []
        f(a)
        l = set(l)
        k = len(l)
        print(a,":",k)



    
    
