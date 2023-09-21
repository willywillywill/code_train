dit = {
    "00":"A",
    "01":"B",
    "100":"0",
    "101":"1",
    "1100":"2",
    "1101":"3",
    "11100":"4",
    "11101":"5",
    "111100":"6",
    "111101":"7",
    "111110":"8",
    "111111":"9"
}

for i in range(int(input())):
    in1 = input()
    lst = []
    n = 0
    while n < len(in1):
        for i in range(n,len(in1)):
            for j in dit:
                if j==in1[n:i+1]:
                    lst.append(dit[j])
                    n=i+1
    if "A" in lst:
        k1 = lst.index("A")
        V_ = lst[k1-1:]
        S_ = lst[:k1-1]
    else:
        k1 = lst.index("B")
        V_ = lst[k1-1:]
        S_ = lst[:k1-1]
    print("%s,%s"%("".join(S_),"".join(V_)))


"""
4
1111001111011111101111111000010001
101110011101110111000010101
11100110111001011110001
111011100110111100110100
"""