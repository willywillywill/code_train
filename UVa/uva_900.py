n = 50
fib = [0 for i in range(n+1)]
fib[1] = 1
fib[2] = 2

for i in range(3,n+1):
    fib[i] = fib[i-1]+fib[i-2]

while 1:
    s = int(input())
    if s==0:
        break
    print(fib[s])