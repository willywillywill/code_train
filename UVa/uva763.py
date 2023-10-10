fib = [0,1]
while fib[-1]+fib[-2] <= 999999999999999999999:
    fib.append(fib[-1]+fib[-2])
del fib[:2]
fib_2num = lambda inx: sum([ fib[i] for i in range(len(inx)) if int(inx[i])])

while 1:
    try:
        in1 = input()[::-1]
        in2 = input()[::-1]
        in3 = input()
        num = fib_2num(in1)+fib_2num(in2)
        fib_i = []
        for i in range(len(fib)-1,-1,-1):
            if fib[i] <= num:
                num -= fib[i]
                fib_i.append("1")
            else:
                if "1" in fib_i:
                    fib_i.append("0")
        print("".join(fib_i))
        print()
    except:
        break