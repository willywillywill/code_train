s1 = [4,6,8]
s2 = ["A","E","H","I","L","M","O","S","T"]
lst = []
for _ in range(int(input())):
    lst.append(input().split())

lst.sort(key=lambda x:(s2.index(x[0][-1]),s1.index(int(x[0][0]))))
for i in lst:
    print("%s: %s"%(i[0][-1],i[1]))