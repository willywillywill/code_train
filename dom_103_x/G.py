txt = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABC")
num = {
    "00":0,
    "01":1,
    "100":2,
    "101":3,
    "1100":4,
    "1101":5,
    "11100":6,
    "11101":7,
    "111100":8,
    "111101":9
}
for _ in range(int(input())):
    in1 = list(input())
    k=0
    out = ""
    while in1:
        if "".join(in1[:k]) in num:
            out += str(num["".join(in1[:k])])
            del in1[:k]
            k=0
        else:
            k+=1
    print(txt[int(out)+2])
"""
3
00100
0111100
1001101

2
00111101
0111101
"""