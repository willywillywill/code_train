import itertools

table = [
    [int("".join(i)) for i in itertools.product("12",repeat=k)]
    for k in range(1,18)
]
for _ in range(int(input())):
    p,q = list(map(int,input().split()))
    out = []
    for i in table[p-1]:
        if i%(2**q)==0:
            out.append(i)
    if out:
        print("Case %d:"%(_+1),*out)
    else:
        print("Case %d: impossible"%(_+1))