for _ in range(int(input())):
    dit = {}
    for i in input().lower():
        if i.isalpha():
            dit[i] = dit.get(i,0)+1
    dit = list(dit.items())
    dit.sort(key=lambda x:(x[1],-ord(x[0])),reverse=True)
    mm = dit[0][1]
    for i in dit:
        if i[1]==mm:
            print(i[0],end="")
    print()

"""
1
Computers account for only 5% of the country's commercial electricity consumption.

"""