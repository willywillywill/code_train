import itertools
import math

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    p = list(itertools.permutations(str(a),len(str(a))))
    b = int("".join(p[b-1]))
    c = int("".join(p[c-1]))
    print(math.gcd(b,c))