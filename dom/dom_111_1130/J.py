# !!!


for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    for i in range(n if n!=1 else 2,m+1):
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            print(i)


    