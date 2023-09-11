codeKey = {
    "A":0, "E":0, "I":0, "O":0, "U":0, "Y":0, "W":0, "H":0,
    "B":1, "P":1, "F":1, "V":1,
    "C":2, "S":2, "K":2, "G":2, "J":2, "Q":2, "X":2, "Z":2,
    "D":3, "T":3,
    "L":4,
    "M":5, "N":5,
    "R":6
}

def f(l, n=-1):
    if n == -len(l):
        return l
    if l[n] == l[n-1]:
        del l[n-1]
    return f(l, n-1)

def f2(l):
    if 0 in l:
        k = l.index(0)
        del l[k]
        return f2(l)
    else:
        return l

r = []
name = []

while 1:
    try:
        s = input()
        name.append(s)
        k = [s[0]]+[codeKey[i] for i in s[1:len(s)]]
        r.append(k)
    except:
        break

print("%-10s%27s"%("NAME", "SOUNDEX CODE"))

for i in range(len(r)):
    k = f(r[i])
    if len(k) >1:
        if codeKey[k[0]] == k[1]:
            del k[1]

    res = f2(k)
    res = res[0:4]

    while len(res) != 4:
        res.append(0)

    res = "".join([ str(j) for j in res ])

    print("%9s%-25s%-8s"%(" ",name[i],res))

print(" "*19+"END OF OUTPUT")
