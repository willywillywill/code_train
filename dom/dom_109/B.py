for _ in range(int(input())):
    in1 = input()
    n = in1[::-1]
    d = sum([ 10**i for i in range(len(n)) if n[i]=="4" ])
    print(int(in1)-d,d)
