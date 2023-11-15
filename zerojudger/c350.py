N,K,W = map(int,input().split())
totall = N
while N>=K:
    n = N//K*W
    totall += n
    N = n+N%K
print(totall)
    