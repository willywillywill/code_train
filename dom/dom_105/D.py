import math

for _ in range(int(input())):
    in1 = list(map(int, input().split(",")))
    k = 0
    for i in range(len(in1)):
        for j in range(len(in1)):
            if i!=j:
                k = max(k, math.gcd(in1[i],in1[j]))
    print(k)