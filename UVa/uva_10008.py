dit = {}
for i in range(int(input())):
    for j in list(input()):
        if j.isalpha():
            dit[j.upper()] = dit.get(j.upper(),0)+1

lst = list(dit.items())
lst.sort(key=lambda x:(x[1],-ord(x[0])),reverse=True)
for i in lst:
    print(i[0],i[1])

"""

"""
