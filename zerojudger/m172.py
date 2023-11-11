def p(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(2)
        continue
    while 1:
        if p(n) and str(n) == str(n)[::-1]:
            print(n)
            break
        n += 1