fib = [0 for i in range(5001)]
fib[0] = 0
fib[1] = 1

for i in range(2,5001):
    fib[i] = fib[i-1]+fib[i-2]

while 1:
    try:
        i = int(input())
        print("The Fibonacci number for %s is %s"%(i,fib[i]))
    except:
        break
