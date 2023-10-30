def f(n):
    if n==1:
        return 3
    if n == 2:
        return 5
    return 3*f(n-1)-f(n-2)

n = int(input())
print(f(n))