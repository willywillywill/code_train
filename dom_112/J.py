def f(i):
    if i==1:
        return 1
    return f(i-1)+(i-1)
while 1:
    try:
        print(f(int(input())))
    except:
        break