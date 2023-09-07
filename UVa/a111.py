N = lambda n1,n2:(n1-n2)**2

while 1:
    n = int(input())
    if n==0:
        break

    total = 0
    for i in range(n):
        total += N(n,i)

    print(total)