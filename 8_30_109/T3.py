
f = lambda n: 1/((n-1)**0.5 + (n)**0.5)
num = 0
for i in range(2,int(input())+1):
    num+= f(i)
print(round(num,4))