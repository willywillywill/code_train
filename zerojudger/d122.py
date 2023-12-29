def f(i):
    if i<5:
        return 0
    i //= 5
    return i+f(i)
while 1:
    try:
        print(f(int(input())))
    except:
        break