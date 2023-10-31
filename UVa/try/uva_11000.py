
while 1:
    a = 1
    b = 0
    n = int(input())
    if n==-1:
        break
    for i in range(n):
        a,b = 1+b,a+b
    print(b,a+b)