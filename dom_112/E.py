n = int(input())
dit = {}
for i in list(map(int,input().split())):
    dit[i] = dit.get(i,0)+1
lst = list(dit.items())
lst.sort(key=lambda x:(x[1],x[0]))
max_n = lst[-1][1]
for i in lst:
    if i[1] == max_n:
        print(i[0],end=" ")
print()
"""
13
1 5 3 9 1 4 0 0 0 1 4 2 4
"""