n = list(input())
"""
XOXXOOOOX
"""
ox = []
for i in range(3):
    ox.append(n[:3])
    del n[:3]

ans = []
for i in range(3):
    if ox[i] == list("OOO"):
        ans.append(1)
    elif ox[i] == list("XXX"):
        ans.append(2)

    if [ ox[j][i] for j in range(3) ] == list("OOO"):
        ans.append(1)
    elif [ ox[j][i] for j in range(3) ] == list("XXX"):
        ans.append(2)

    if [ ox[j][j] for j in range(3) ] == list("OOO"):
        ans.append(1)
    elif [ ox[j][2-j] for j in range(3) ] == list("XXX"):
        ans.append(2)

if ans.count(1) > ans.count(2):
    print(1)
elif ans.count(1) < ans.count(2):
    print(2)
else:
    print(3)    