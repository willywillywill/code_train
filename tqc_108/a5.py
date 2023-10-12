n = int(input())
lst = []
for i in range(2, n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        if str(i) == str(i)[::-1]:
            lst.append(i)
l = 1
o = 0
u = 0
for i in range(len(lst)):
    print("%-4d"%(lst[i]),end="")
    u = 1
    o+=1
    if l==o:
        u=0
        print()
        l+=1
        o=0
if u:
    print()
print(sum(lst))