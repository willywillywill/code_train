k = input()
p = input()

c =   [ 
    k[j]+"".join([ p[i] for i in range(j,len(p),len(k)) ]) 
    for j in range(len(k))
    ]
c.sort(key=lambda x:x[0])
for i in c:
    print(i[1:],end="")