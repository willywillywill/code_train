# like Fib !!!

def f(i):
    if in1[i] == "/":
        n = 0
        if len(in1) > i+1:
            n += 10 if in1[i+1] == "X" else f(i+1)
        return (10-f(i-1))+n
    elif in1[i] == "X":
        n = 0
        if len(in1) > i+1:
            n += 10 if in1[i+1] == "X" else f(i+1)
        if len(in1) > i+2:
            if in1[i+2] == "X":
                n += 10
            elif in1[i+2] == "/":
                n += 10-f(i+1)
            else:
                n += f(i+2)   
        return 10+n
    else:
        return int(in1[i])   
for _ in range(int(input())):
    in1 = list(map(str, input().split()))    
    d = [ [0,0] for i in range(10)]
    k = in1.copy()
    for i in range(9):
        l = in1.pop(0)
        if l=="X":
            d[i] = [" ",l]
        else:
            d[i][0] = l
            d[i][1] = in1.pop(0)
    d[-1] = [ i for i in in1 ]
    in1 = k.copy()
    if len(d[-1]) == 3:
        k = k[:-2] if k[-3]=="X" else k[:-1]
    m = [ f(i) for i in range(len(k)) ]
    print(sum(m))