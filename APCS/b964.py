n = int(input())
lst = list(map(int,input().split()))
lst.sort()
a1 = -1
a2 = -1
for i in lst:
    if i < 60:
        a1 = i
    else:
        a2 = i
        break
print(*lst)
print(a1 if a1!=-1 else "best case" )
print(a2 if a2!=-1 else "worst case")