import itertools

in1 = list(map(int,input().split(",")))
lst = list(itertools.permutations(in1,6))

for i in lst:
    if sum(i[:3])==sum(i[3:]):
        print(1)
        break
else:
    print(0)