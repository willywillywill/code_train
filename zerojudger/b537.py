def f(a,b):
    if a==b:
        return 1
    if a > b:
        return f(a-b,b)<<1
    return f(b,a)+1

while 1:
    try:
        a,b = map(int,input().split())
        print(f(a,b))
    except:
        break