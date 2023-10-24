n = input()
"""
OOX
OXO
XOO
"""
ans = []

if n[::3] == "OOO":
    ans.append(1)
elif n[::3] == "XXX":
    ans.append(2)

if n[1::3] == "OOO":
    ans.append(1)
elif n[1::3] == "XXX":
    ans.append(2)

if n[2::3] == "OOO":
    ans.append(1)
elif n[2::3] == "XXX":
    ans.append(2)

if n[::4] == "OOO":
    ans.append(1)
elif n[::4] == "XXX":
    ans.apppend(2)
    
if n[2:-2:2] == "OOO":
    ans.append(1)
elif n[2:-2:2] == "XXX":
    ans.append(2)

if ans.count(1) > ans.count(2):
    print(1)
elif ans.count(1) < ans.count(2):
    print(2)
else:
    print(3)
