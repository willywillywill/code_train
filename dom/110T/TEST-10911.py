def p(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    for i in range(n-1,1,-1):
        if p(i):
            print(i)
            break
    else:
        print(2)

