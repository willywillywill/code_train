n = 1024
premi = [1] *(n+1)
for i in range(2, int(n**0.5)+1):
    if premi[i]:
        for j in range(i*i, n+1, i): # 倍數 2,3 ... 
            premi[j] = 0
premi = [ i for i in range(2, n+1) if premi[i] ]
    

print(premi)