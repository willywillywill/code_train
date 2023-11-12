lst = []
for _ in range(int(input())):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x:x[2])
date = [ [] for i in range(7) ]
ans = 0
while lst:
    d,s,e = lst.pop(0)
    d -= 1
    if len(date[d])==0 or (len(date[d]) and s >= date[d][-1][1]):
        date[d].append([s,e])
        ans += 1
print(ans)

"""
5
1 1 10
2 3 4
2 3 5
3 7 8
3 8 9
"""