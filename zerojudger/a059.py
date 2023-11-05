for _ in range(int(input())):
    a = int(input())
    b = int(input())
    num = 0
    for i in range(a,b+1):
        if int(i**0.5)**2 == i:
            num += i
    print("Case %d:"%(_+1),num)