n = "OOXOXOXOO"
"""
OOX
OXO
XOO
"""
lst = [ list(n[i:i+3]) for i in range(0,len(n),3) ]

ans1 = []
for i in range(len(lst)):
    A = [ ii[i] for ii in lst ]
    if ["O","O","O"] == A:
        ans1.append(1)
    elif ["X","X","X"] == A:
        ans1.append(2)

A = [ lst[i][i] for i in range(len(lst)) ]
if A == ["O","O","O"]:
    ans1.append(1)
elif A == ["X","X","X"]:
    ans1.append(2)

A = [ lst[i][2-i] for i in range(len(lst)) ]
if A == ["O","O","O"]:
    ans1.append(1)
elif A == ["X","X","X"]:
    ans1.append(2)

for i in lst:
    if i == ["O","O","O"]:
        ans1.append(1)
    elif i == ["X","X","X"]:
        ans1.append(2)
if 1 in ans1 and 2 in ans1:
    print(3)
else:
    print(*ans1)
