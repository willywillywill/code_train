# OK
while 1:
    try:
        x, y = list(map(int, input().split()))
        l = []

        for _ in range(x):
            k = list(map(int,input().split()))
            l.append(k)
        l = list(zip(*l))  # ??

        for i in l:
            for j in i:
                print(j, end=" ")
            print()
    except:
        break

"""
for i in range(y):
    p = []
    for j in range(x):
        p.append(str(l[j][i]))

    print(" ".join(p))
"""

