lst = []
for _ in range(int(input())):
    m = list(map(int,input().split()))
    for i in range(len(m)):
        if m[i] in [1,14,27,40]:
            m[i] = 1
        elif ((m[i]%14)+(m[i]//14)) > 10:
            m[i] = 10
        else:
            m[i] = (m[i]%14)+(m[i]//14)
    lst.append(m)

for i in lst:
    sum_v = 0
    for j in i:
        if sum_v == 21:
            continue
        if j==1:
            sum_v += 1 if sum_v+11 > 21 else 11
        else:
            sum_v += j
    if sum_v > 21:
        print("F")
    else:
        print(sum_v)
"""
5
3 44
6 12 1
26 25 2
14 27
40 43

3
15 18 2
14 21
1 13 26
"""