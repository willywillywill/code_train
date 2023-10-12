def f_s(s):
    global off
    s = s.replace("(","")
    s = s.replace(")","")
    s = s.split(",")
    if s[1] in dit:
        off = 1
    dit[s[1]] = int(s[0])
while 1:
    try:
        dit = {}
        off = 0
        in1 = list(map(f_s, input().split()[:-1]))
        if off or "" not in dit:
            print("not complete")
            break
        queue = [""]

        out = []
        while queue:
            node = queue.pop(0)
            out.append(str(dit[node]))
            del dit[node]
            if node+"L" in dit:
                queue.append(node+"L")
            if node+"R" in dit:
                queue.append(node+"R")
        if len(dit):    
            print("not complete")
        else:
            print(" ".join(out))
    except:
        break

"""
(11,LL) (7,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(3,L) (4,R) ()
(11,LL) (7,LLL) (2,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(5,) (3,) (4,R) ()
(5,) (3,LL) ()
"""