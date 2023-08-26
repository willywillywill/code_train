
while 1:
    try:
                
        n, c = list(map(int, input().split()))

        k = [ i for i in range(1,n+1) if len([ j for j in range(1,i+1) if i%j==0 ])<=2 ]
        len_k = len(k)

        if len_k % 2:
            print("%d %d:"%(n,c),*k[(len_k//2)-(c*2-1)//2 : (len_k//2)+((c*2-1)//2)+1])
        else:
            print("%d %d:"%(n,c),*k[(len_k//2)-(c*2)//2 : (len_k//2)+((c*2)//2)])
        print()
    except:
        break

