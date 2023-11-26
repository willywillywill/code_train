def H(n):
    res = 0
    for i in range(1, n+1):
        res = res+n//i
    return res

for _ in range(int(input())):
    print(H(int(input())))