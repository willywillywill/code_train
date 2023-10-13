# 16:20
# 8:22

n = int(input())

def p(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

lst = [str(n)]
while n:
    l = 99999999
    for i in range(2,n):
        if p(i) and p(n-i):
            l = min(l,abs(i-(n-i)))
    n = l
    lst.append(str(l))
    if l==0 or l==2:
        break

for i in lst:
    print(i,end=",")
print()