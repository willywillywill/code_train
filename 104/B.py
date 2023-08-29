import itertools

out = []
n = int(input())
ok = set(map(int, input().split(",")))
for _ in range(n):
    test = list(map(int, input().split(",")))

    test = list(itertools.permutations(test, 5))
    test = set( tuple(sorted(list(i))) for i in test )
    test = [ set(i) for i in test ]

    dit = {2:0, 3:0, 4:0, 5:0}
    for i in range(len(test)):
        num = len(test[i] & ok)
        dit[num] = dit.get(num,0)+1
    out.append(dit)

while out:
    o = out.pop(0)
    for i in range(2,6):
        print(o[i],end= "," if i!=5 else "")
    print()