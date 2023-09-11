# https://program-think.blogspot.com/2011/12/prime-algorithm-1.html

# 1
prime = lambda x: True if len([ i for i in range(2,x) if x%i==0 ])==0 else False
prime_lst = lambda n: [ i for i in range(2,n) if prime(i) ]
# 4
prime = lambda x: True if len([ i for i in range(2,int(x**0.5)+1) if x%i==0 ])==0 else False
prime_lst = lambda n: [ i for i in range(2,n) if prime(i) ]

#5
n = 25
premi = [1] *(n+1)
for i in range(2, int(n**0.5)+1):
    if premi[i]:
        for j in range(i*i, n+1, i): # 倍數 2,3 ... 
            premi[j] = 0

premi = [ i for i in range(2, n+1) if premi[i] ]
print(premi)
