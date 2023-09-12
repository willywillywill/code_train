s = input()
dit = {}
for i in s:
    i = ord(i)
    dit[i] = dit.get(i, 0)+1
lst = list(dit.items())
lst.sort(key=lambda x:(x[1],-x[0]))
for n,m in lst:
    print(n,m)