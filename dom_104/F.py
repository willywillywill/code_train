for _ in range(int(input())):
    s = int(input())
    s = bin(s)[2:]
    j = 0
    for i in s:
        j += int(i)
    
    print(j)

