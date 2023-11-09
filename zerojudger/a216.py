while 1:
    try:
        n = int(input())
        f = 0
        g = 0
        for i in range(1,n+1):
            f += i  # f(n) = n + f(n-1) 求和
            g += f  # g(n) = f(n) + g(n-1)
        print(f,g)
    except:
        break