def p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
while 1:
    try:
        n,c = list(map(int,input().split()))
        lst = [1]+[ i for i in range(2,n+1) if p(i) ]
        k = len(lst)
        print("%d %d: "%(n,c),end="")
        if k < 2*c-1:
            print(*lst)
        elif k%2==0:
            x = (k-c*2)//2
            print(*lst[x:k-x])
        else:
            x = (k-c*2+1)//2
            print(*lst[x:k-x])
        print()
    except:
        break


"""
21 2
"""