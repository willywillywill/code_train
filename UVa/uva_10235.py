def p(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

while 1:
    try:
        n = int(input())
        if p(n):
            if p(int(str(n)[::-1])) and str(n) != str(n)[::-1]:
                print(n,"is emirp.")
            else:
                print(n,"is prime.")
        else:
            print(n,"is not prime.")
    except:
        break
