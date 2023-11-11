
for _ in range(int(input())):
    n = list(input())
    m = []
    while n:
        s = n.pop(0)
        if s in "+-*/":
            m.append(s)
        else:
            k = s
            while s not in "+-*/" and n:
                s = n.pop(0)
                k += s
            if len(k)>1:
                m.append(k[:-1])
                m.append(k[-1])
            else:
                m.append(k)
    n = m
    while "+" in n or "-" in n:
        for i in range(len(n)):
            if n[i]=="+" or n[i]=="-":
                k1 = n.pop(i-1)
                k2 = n.pop(i-1)
                k3 = n.pop(i-1)
                n.insert(i-1,str(eval(k1+k2+k3)))
                break

    while "*" in n or "/" in n:
        for i in range(len(n)):
            if n[i]=="*" or n[i]=="/":
                k1 = n.pop(i-1)
                k2 = n.pop(i-1).replace("/","//")
                k3 = n.pop(i-1)
                n.insert(i-1,str(eval(k1+k2+k3)))
                break


    print(n[0])