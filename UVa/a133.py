N1,N2 = list(map(int, input().split()))

if N2>N1:
    N1,N2 = N2,N1
    L2 = list(map(int,input().split()))
    L1 = list(map(int,input().split()))
else:
    L1 = list(map(int,input().split()))
    L2 = list(map(int,input().split()))



for i in range(N2):
    for j in range(i+1):
        if L2[i] == L1[j]:
            pass  