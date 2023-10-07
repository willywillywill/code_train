"""
3
8
48
126
"""
for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(1)
        continue
    m = 1
    lst = []
    for i in range(9,1,-1):
        while n%i==0:  # ex:100 455 (55)
            n //=i
            m *= i
            lst.append(str(i))
    if len(lst)==0 or n>1:
        print(-1)
    else:
        print("".join(lst[::-1]))