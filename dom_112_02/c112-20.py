n = int(input())
lst = []
ans = 1
for i in range(1,n+1):
    if n%i==0:
        if i==3 or i==5:
            ans = 0
        lst.append(i)

if len(lst) >= 5 and ans:
    print(1)
else:
    print(0)