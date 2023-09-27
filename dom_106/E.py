for _ in range(int(input())):
    in1 = list(map(str, input().split("/")))
    r1 = list(map(int, in1[0].split(".")))
    r2 = list(map(int, in1[1].split(".")))
    r3 = []
    for i in r2:
        a = list(bin(i))[2:]
        if a==["0"]:
            a = list("00000000")
        for j in range(len(a)):
            a[j] = "0" if a[j]=="1" else "1" 
        r3.append(int("".join(a),2))

    out = []
    for i in range(4):
        b = r1[i]&r2[i]|r3[i]
        out.append(str(b))
    print(".".join(out))


"""
5
139.175.153.252/255.255.0.0
10.104.69.0/255.255.255.192
192.15.156.205/255.255.255.224
192.168.10.65/255.255.255.224
10.240.168.19/255.255.192.0 
"""