
p,d = 1,28
n= 0
for i in range(1,int(d**0.5)+1):
    if d%i==0:
        n = i
m = d//n
for i in range(n,m+1):
    print(i)