while 1:
    try:
        s = list(input().split())
    except:
        break
    total = 0

    for i in s:
        c = 0
        for j in i:
            if ("A" <= j <= "Z") or ("a" <= j <= "z"):
                if c==0:
                    total += 1
                    c=1
            else:
                if c==1:
                    c=0
    print(total)

