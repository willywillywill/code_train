def f_s(s):
    global off
    s = s.replace("(","")
    s = s.replace(")","")
    s = s.split(",")
    if s[1] in dit:
        off = 1
    dit[s[1]] = int(s[0])

dit = {}
off = 0
in1 = list(map(f_s, input().split()[:-1]))
node_num = len(dit)
if off or "" not in dit:
    print("not complete")
    continue
queue = [""]
visited_num = 0
out = []
while queue:
    node = queue.pop(0)
    visited_num += 1
    out.append(str(dit[node]))
    del dit[node]
    if node+"L" in dit.keys():
        queue.append(node+"L")
    if node+"R" in dit.keys():
        queue.append(node+"R")
print(visited_num,node_num)
if visited_num != node_num:
    print("not complete")
else:
    print(" ".join(out))

"""
(11,LL) (7,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(3,L) (4,R) ()
(11,LL) (7,LLL) (2,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(5,) (3,L) (4,R) ()
"""