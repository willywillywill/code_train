def fib(i):
    if i==1:
        return 1
    return fib(i-1)+(i-1)

while 1:
    try:
        print(fib(int(input())))
    except:
        break