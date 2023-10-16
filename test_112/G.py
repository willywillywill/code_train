
def f(i):
    if i==1:
        return 1
    return f(i-1)+i**2

while 1:
    n = int(input())
    if not n:
        break
    print(f(n))