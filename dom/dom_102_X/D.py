import itertools
import math

for _ in range(int(input())):
    in1,in2,in3 = input().split(", ")
    in2 = int(in2)
    in3 = int(in3)
    in1 = list(itertools.permutations(in1,len(in1)))
    in1 = [ "".join(i) for i in in1 ]
    print(math.gcd(int(in1[in2-1]),int(in1[in3-1])))

"""
3
1234, 15, 9
1234, 3, 4
1234, 2, 5
"""