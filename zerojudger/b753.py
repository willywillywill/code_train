local_table = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
        'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
        'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
x = [1,9,8,7,6,5,4,3,2,1,1]

while 1:
    try:
        r = []
        dit = {"T":0,"O":0,"F":0}
        for _ in range(int(input())):

            lst = input()
            if lst[1] not in ["1","2"]:
                dit["F"] += 1
            else:
                if lst in r:
                    dit["O"] += 1
                else:
                    a = lst[0]
                    b = lst[1:]
                    b = list(str(local_table[a]))+list(b)
                    b = [ x[i]*int(b[i]) for i in range(11) ]
                    b = sum(b)
                    b = b%10
                    if b:
                        dit["F"] += 1
                    else:
                        dit["T"] += 1
                        r.append(lst)
        p = [ str(dit["T"]), str(dit["O"]), str(dit["F"]) ]
        print(",".join(p))
    except:
        break