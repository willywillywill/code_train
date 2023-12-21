for _ in range(int(input())):
    n = int(input())
    mod = n%2
    if mod==0:
        a = "1"
        n -= 2
    else:
        a -= "7"
        n -= 3
    b = (n//2)*"1"
    print(a+b)