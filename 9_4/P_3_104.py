import itertools

for _ in range(int(input())):
    s = list(map(int, input().split(",")))
    k = list(itertools.permutations(str(s[0])))
    num = [ k[s[1]-1],k[s[2]-1] ]
    num = [ int("".join(i)) for i in num ]
    print(sum(num))

"""
12,1,2
"""