def f_s(s:str):
    s = s.replace("{","")
    s = s.replace("}","")
    s = tuple(map(int,s.split(",")))
    return set(s)

for _ in range(int(input())):
    in1 = list(map(f_s,input().split("}, {")))
    t1 = in1[0]
    t2 = in1[1]

    or_ = t1.union(t2)
    and_ = t1.intersection(t2)
    x_ = t1-t2
    xor_ = t1^t2
    out = [or_,and_,x_,xor_]
    out = [ str(i) if i else "N" for i in out ]
    print(", ".join(out))
"""
{1, 3}, {2, 4}

{1, 2, 3, 4}, N, {1, 3}, {1, 2, 3, 4}
"""