dit = {}
s = list(input().replace(" ", ""))

while s:
    ss = s.pop(0)
    dit[ss] = dit.get(ss,0)+1
lst = list(dit.items())
lst.sort(key= lambda n: n[1], reverse=True)

out1 =sum([ lst[i][1] for i in range(5)])
out2 ="".join([ lst[i][0] for i in range(5)])
print(out1)
print(out2)

"""
Failure is the mother of success.
"""