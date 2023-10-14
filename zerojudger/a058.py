n = int(input())

k1 = 0
k2 = 0
k3 = 0

for i in range(n):
    p = int(input())

    if p%3 == 0:
        k1 += 1
    elif p%3 ==1:
        k2 += 1
    elif p%3 ==2:
        k3 += 1
print(k1,k2,k3)