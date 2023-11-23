lst = []
for _ in range(int(input())):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x:(x[1],x[2],-x[0]),reverse=True)

for i in lst:
    print(*i)