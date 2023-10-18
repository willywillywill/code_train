for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    ans = 0

    for j in range(n-1):
        for i in range(1,n):
            if lst[i-1]>lst[i]:
                lst[i-1],lst[i] = lst[i],lst[i-1]
                ans+=1
    print("Optimal train swapping takes %d swaps."%(ans))