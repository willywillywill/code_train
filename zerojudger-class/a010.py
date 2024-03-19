n = int(input())
d = {}
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n = n//i
            d[i] = d.get(i, 0)+1
            break
out = ""
for i in d:
    if d[i]!=1:
        out += f"{i}^{d[i]} * "
    else:
        out += f"{i} * "
print(out[:-2])