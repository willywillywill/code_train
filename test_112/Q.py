a,q = list(map(int,input().split()))
lst = [ i for i in range(1,a+1) ]
in1 = []

for i in range(q):
    n,m = list(map(int,input().split()))
    lst[n-1],lst[m-1] = lst[m-1],lst[n-1]
    ans=0
    
    for j in range(len(lst)):
        for k in range(j,len(lst)):
            if lst[j]>lst[k]:
                ans+=1

    print(ans)


"""
5 4
4 5
2 4
2 5
2 2

6 7
1 4
3 5
2 3
3 3
3 6
2 1
5 1
"""