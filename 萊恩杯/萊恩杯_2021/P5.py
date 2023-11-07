in1 = list(input())

while in1:
    s = in1.pop(0)

    if s.isdigit():
        n = int(s)
        ss = ""
        s = in1.pop(0)
        while 1:
            s = in1.pop(0)
            if s == "]":
                break
            ss += s
        print(ss*n, end="")
    else:
        print(s,end="")



"""
ab2[c]ba
"""
        