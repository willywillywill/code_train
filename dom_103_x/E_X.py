
for _ in range(int(input())):
    in1 = list(map(int,input().split()))
    inC = in1.copy()
    inT = sorted(in1.copy())
    inG = [ (i%14)+(i//14) for i in in1 ]

    G_dit = {}
    T_num = 1
    C_dit = { "b":0, "r":0, "s":0, "f":0}

    while inG: # 同點
        k1 = inG.pop(0)
        k1_n = 1
        while (k1 in inG):
            del inG[inG.index(k1)]
            k1_n+=1
        G_dit[k1_n] = G_dit.get(k1_n, 0)+1
    for i in range(1,len(inT)): # 連續
        if inT[i] == inT[i-1]+1:
            T_num+=1

    for i in inC: # 同色
        if i <= 13:
            C_dit["b"] += 1
        elif i <= 26:
            C_dit["r"] += 1
        elif i <= 39:
            C_dit["s"] += 1
        else:
            C_dit["f"] += 1

    if T_num == 5:
        for i in C_dit:
            if C_dit[i]==5:
                print(7)
                break
        else:
            print(4)
    elif max(G_dit) == 4:
        print(6)
    elif max(G_dit) == 3:
        if 2 in G_dit:
            print(5)
        else:
            print(3)
    elif max(G_dit) == 2:
        if G_dit[2]==2:
            print(2)
        else:
            print(1)
    else:
        print(0)

    
"""
3 44 4 6 7 5 
19 12 1 32 45 25

14 16 18 19 20 21 
"""