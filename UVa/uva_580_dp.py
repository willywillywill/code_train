# https://blog.csdn.net/mobius_strip/article/details/43851679
f = [[ 0 for j in range(8)]for i in range(31)]

for i in range(4):
    f[2][i] = 1
for i in range(3,31):
    f[i][0] = f[i-1][2]
    f[i][1] = f[i-1][0]+f[i-1][2]
    f[i][2] = f[i][3] = f[i-1][1]+f[i-1][3]

while 1:
    in1 = int(input())
    if in1==0:
        break
    if in1<3:
        print(0)
        continue
    ans = 1<<in1 # 2**in1
    for i in range(4):
        ans -= f[in1][i]
    print(ans)