# https://ithelp.ithome.com.tw/articles/10263029?sc=pt
for _ in range(int(input())):
    in1 = int(input())
    fib = [0,1]
    while fib[-1]+fib[-2] <= in1:
        fib.append(fib[-1]+fib[-2])
    del fib[:2]
    print(in1,end="=")
    for i in range(len(fib)-1,-1,-1):
        if in1 >= fib[i]:
            in1 -= fib[i]
            print(1,end="")
        else:
            print(0,end="")
    print() 