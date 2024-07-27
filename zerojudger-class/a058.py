m1 = 0
m2 = 0
m3 = 0
for _ in range(int(input())):
    n = int(input())
    if n%3==0:
        m1 += 1
    elif n%3==1:
        m2 += 1
    else:
        m3 += 1

print(m1,m2,m3)
