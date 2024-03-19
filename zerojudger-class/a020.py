"""
T112663836
"""

d = {
    "A":10, "J":18 ,"S":26,
    "B":11, "K":19, "T":27,
    "C":12, "L":20, "U":28,
    "D":13, "M":21, "V":29,
    "E":14, "N":22, "W":32,
    "F":15, "O":35, "X":30,
    "G":16, "P":23, "Y":31,
    "H":17, "Q":24, "Z":33,
    "I":34, "R":25,
}

# str -> list
# becaus: n.pop(0)
n = list(input())

"""
n = list(str)+list
d[n.pop(0)]] <- int

int -> str -> list
OK : 27(int) -> "27"(str) -> ["2", "7"](list(str))
ER : 27(int) -> [27](list(int))

because:
    k = n.pop(0)
so:
    k not in new_n(+n)

"""
n = list(str(d[n.pop(0)]))+n

# list(str) -> list(int) & reverse
n = list(map(int,n[::-1]))

k2 = [ n[i]*i for i in range(1,10) ]
k2 = sum(k2)+n[0]+n[-1]

if k2%10==0:
    print("real")
else:
    print("fake")
