# 16:20
n = int(input())
def p(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
out = [n]
while 1:
    lst = []
    for i in range(2,n):
        if p(i) and p(n-i):
            lst.append([i,n-i, abs((i-(n-i)))])
    lst.sort(key=lambda x:x[2],reverse=True)
    n = lst[-1][-1]
    out.append(n)
    if out[-1]==2 or out[-1]==0:
        break
for i in out:
    print(i,end=",")