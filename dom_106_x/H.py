
for _ in range(int(input())):
    in1 = input().split()
    in1 = list(in1)
    out = []
    while in1:
        k = in1.pop(0)
        if k in "+-*/":
            a1 = out.pop(-2)
            a2 = out.pop(-1)
            out.append(str(int(eval(a1+k+a2))))
        else:
            out.append(k)
    print(out[0])


"""
3
3 5 +
9 2 3 5 + * +
6 3 / 1 4 - * 3 + 8 -

3
2 3 + 4 *
2 3 4 + * 5 *
2 123 -
"""