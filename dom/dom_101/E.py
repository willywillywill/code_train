

id = {
    "T":[],"O":[],"F":[]
}
lst = list("ABCDEFGHJKLMNPQRSTUVXYWZI")
dit = {}
for i,j in enumerate(lst):
    dit[j] = str(10+i)
lst = [1,9,8,7,6,5,4,3,2,1,1]

for _ in range(int(input())):
    in1 = list(input())
    if int(in1[1])>2:
        id["F"].append(in1)
        continue
    id_v = in1.copy()
    d = in1.pop(0)
    in1.insert(0,dit[d[0]][1])
    in1.insert(0,dit[d[0]][0])

    for i in range(len(in1)):
        in1[i] = int(in1[i])*lst[i]

    if sum(in1) % 10 == 0:
        if id_v in id["T"]:
            id["O"].append(id_v)
        else:
            id["T"].append(id_v)
    else:
        id["F"].append(id_v)
    
print("%d,%d,%d"%(len(id["T"]),len(id["O"]),len(id["F"])))
"""
8
M123456789
A123456789
A323456783
M123456789
M123456789
M123456789
Y123456788
A223344556

4
R102345678
A108881111
A108881111
B101111111
"""