# 5:16

n = int(input())

def p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

lst = [ i for i in range(2,n) if p(i) and str(i)==str(i)[::-1] ]

k = 1
l = 0
j = 0
for i in range(len(lst)):
    print("%-4d"%(lst[i]),end="")
    j=1
    l+=1
    if k==l:
        k+=1
        l=0
        j=0
        print()
if j:
    print()
print(sum(lst))