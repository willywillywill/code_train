dit = {}
for _ in range(int(input())):
    lst = list(map(str,input().split()))[0]
    dit[lst] = dit.get(lst,0)+1

dit = list(dit.items())
dit.sort(key=lambda x:x[0])
for i in dit:
    print(i[0],i[1])

"""
3
Spain Donna Elvira
England Jane Doe
Spain Donna Anna
"""