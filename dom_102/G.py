
for _ in range(int(input())):
    in1 = list(map(str,input().replace("-","")))
    in1,chick = list(map(int,in1[:-1][::-1])),in1[-1]

    s = 0
    if len(in1) == 9:
        for i in range(9):
            s += in1[i]*(i+2)
        s %= 11
        n = 11-s
        if n==11:
            n = "0"
        elif n==10:
            n = "X"
        else:
            n = str(n)
    else:
        for i in range(12):
            s += in1[i]*( 1 if i%2 else 3 )
        s %= 10
        n = 10-s
        if n == 10:
            n = "0"
        else:
            n = str(n)
    print( "T" if n==chick else "F" )


"""
6
0-201-55802-5
9780201558029
986-276-566-6
978-986-276-566-1
957-442-355-7
957-442-355-4

4
986-7693-40-X
978-986-7693-40-2
7-309-04547-5
7-309-04547-1
"""