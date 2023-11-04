for _ in range(int(input())):
    n = input()
    b1 = bin(int(n,10)).count("1")
    b2 = bin(int(n,16)).count("1")
    print(b1,b2)
