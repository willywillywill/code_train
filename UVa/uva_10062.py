
while 1:
    try:
        s = input()
        dit = {}
        for i in s:
            dit[ord(i)] = dit.get(ord(i),0)+1
        lst = sorted(list(dit.items()), key= lambda x:(x[1],-x[0]))
        for i in lst:
            print(i[0],i[1])
    except:
        break