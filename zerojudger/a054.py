table = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
            'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
            'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}


n = list(map(int,input()))
s = 0
for i in range(8):
    s += n[i]*(8-i)
for i in table:
    a = [ int(j) for j in list(str(table[i])) ]
    if n[8] == 0:
        if (s+a[0]+a[1]*9)%10 == 0:
            print(i, end="")
    else:
        if 10-(s+a[0]+a[1]*9)%10 == n[8]:
            print(i, end="")

