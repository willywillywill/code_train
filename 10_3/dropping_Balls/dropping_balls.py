
for _ in range(int(input())):
    D, I = list(map(int, input().split()))
    k = 1
    for i in range(D-1):
        if I%2: # left
            k = 2*k
            I = (I+1)/2
        else:   # right
            k = 2*k+1
            I = I/2
    print(k)


"""
5
4 2
3 4
10 1
2 2
8 128

12
7
512
3
255
"""