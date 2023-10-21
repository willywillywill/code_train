s = input()
dit = {}
for i in s:
    dit[ord(i)] = dit.get(ord(i),0)+1
lst = sorted(list(dit.items()),reverse=True, key= lambda x:(x[0]))