# OK

import math
import itertools

for _ in range(int(input())):
    l = list(map(int, input().split()))
    k = []
    for i,j in itertools.combinations(l,2):
        k.append(math.gcd(i,j))

    print(max(k))
