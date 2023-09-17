fib = [0,1]

n = 20
while fib[-1]+fib[-2] <= n:
    fib.append(fib[-1]+fib[-2])
del fib[:2]

m = n



k = len(fib)-1
while m:
    if fib[k] <= m:
        m -= fib[k]
        print(fib[k])
