"""
4
222222222222222222222222222, 555555555555555555555555555, 111111111111111, 44444444444444444444444444444444444444444444444444444, 33333333333333333333333333333333333333333333
123456789, 123456787, 123456788
3333333333333333333333333, 1111111111111111111111111, 2469135802469135802469135308641975308641975308642
44444444444444444444444444444444444444444444444444444, 111111111111111, 222222222222222222222222222, 33333333333333333333333333333333333333333333

3
4, 2, 1, 5
1, 2, 3, 4, 5, 6
7, 6, 5, 4, 3, 2
"""
for _ in range(int(input())):
    in1 = list(map(int, input().split(",")))
    k = in1.copy()
    in1.sort()
    out = []
    while k:
        d = k.pop(0)
        out.append(str(in1.index(d)+1))
    print(", ".join(out))
