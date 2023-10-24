n = list(input())
ans = 0
for i in range(len(n)+1):
    for j in range(len(n)+1):
        k = [ i for i in n ]
        k.insert(i,"3")
        k.insert(j,"5")
        if int("".join(k))%3==0 and int("".join(k))%7==0:
            ans = 1
print(ans)