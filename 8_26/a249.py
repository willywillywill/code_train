"""
for _ in range(int(input())):
    D,I = list(map(int, input().split()))

    lst = [ i for i in range(2**(D-1),2**D) ]

    for i in range(I-1):
        if I%2==0:
            lst = lst[len(lst)//2:len(lst)]
        else:
            lst = lst[0:len(lst)//2]

    print(lst[0])
"""

for _ in range(int(input())):
    D, I = map(int,input().split())
    idx = 1  # root
    remainder = I  # L or R
    for i in range(D-1):
        if remainder % 2==1:
            idx = 2*idx
            remainder = (remainder+1)//2
        else:
            idx = 2*idx+1
            remainder=remainder//2
    print(idx)
