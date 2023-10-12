# ! ! ! LCS
k = []
while 1:
    s = int(input())
    if s==-9999:
        break
    k.append(s)
lst = []
for i in range(len(k)):
    l = []
    for j in range(i,len(k)):
        if len(l)==0:
            l.append(k[j])
        else:
            l.append(k[j]+l[-1])
    lst.append(l)
out = 0
for i in lst:
    for j in i:
        out = max(out,j)
print(out)
"""
-3 
5 
-2 
1 
-4 
-9999
"""