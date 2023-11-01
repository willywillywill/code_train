def f(i):
    if int(i)<10:
        return i
    return f(str(sum([ int(j) for j in str(i)])))

while 1:
    n = int(input())
    if not n:
        break
    print(f(n))