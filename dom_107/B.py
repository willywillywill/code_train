"""
3
122
110
102
211
220
201
111
220
201

4
122
110
201
212
122
121
121
021
002
121
000
000
"""

for _ in range(int(input())):
    lst = []
    for i in range(3):
        lst.append(list(map(int, input())))
    a1 = [[ lst[ii][i] for ii in range(len(lst)) ] for i in range(3) ]
    a2 = [ lst[i]  for i in range(3) ]
    a3 = [ lst[i][i] for i in range(len(lst)) ]
    a4 = [ lst[i][abs(i-2)] for i in range(len(lst)) ]

    out = 0
    if not out:
        for i in a1:
            if i[0] == i[1] == i[2]:
                out = i[0]
    if not out:
        for i in a2:
            if i[0] == i[1] == i[2]:
                out = i[0]
    if not out:
        out = a3[0] if a3[0] == a3[1] == a3[2] else 0
    if not out:
        out = a4[0] if a4[0] == a4[1] == a4[2] else 0
    if out:
        print(out)
    else:
        print(3)
