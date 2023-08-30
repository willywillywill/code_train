
f = lambda n: (-1)**(n+1) / ((2*n)-1)
num = 0
n = int(input())
for i in range(1, n+1):
    num += f(i)
num*=4
print(round(num, 4))