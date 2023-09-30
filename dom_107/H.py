def del_s(s):
    s = s.replace("[","")
    s = s.replace("]","")
    return s
def dfs(n,l):
    a1,a2 = in1[n]
    if a1 in l:
        return
    l.append(a1)
    if a1==a2:
        st1.append(a1)
        return 
    else:
        st1.append(a1)
        dfs(a2-1, l.copy())    

for _ in range(int(input())):
    in1 = list(map(int, del_s(input()).split(",")))
    in2 = in1.copy()
    in1 = [ [i+1,in1[i]] for i in range(len(in1)) ]
    o = []
    for i in range(len(in2)):
        st1 = []
        dfs(i,[])
        o.append(st1)

    out = []
    for i in range(len(o)):
        if set(o[i]) not in [ set(ii) for ii in out ]:
            out.append(o[i])

    print(out)

"""
4
[1, 6, 7, 4, 2, 3, 5, 8]
[1, 6, 3, 4, 7, 2, 5, 8]
[1, 6, 5, 4, 7, 3, 2, 8]
[1, 6, 8, 4, 7, 3, 5, 2]

[[1], [2, 6, 3, 7, 5], [4], [8]]
[[1], [2, 6], [3], [4], [5, 7], [8]]
[[1], [2, 6, 3, 5, 7], [4], [8]]
[[1], [2, 6, 3, 8], [4], [5, 7]]
"""