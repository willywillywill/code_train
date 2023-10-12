# me
def f_s(s):
    global max_layer
    s = s.replace("(","")
    s = s.replace(")","")
    s = s.split(",")
    k=1
    for i in s[1]:
        if i=="L":
            k = k*2
        else:
            k = k*2+1
    max_layer = max(max_layer, len(s[1]))
    s = int(s[0]),k
    return s

while 1:
    try:
        max_layer = 0
        in1 = list(map(f_s, input().split()[:-1]))
        lst = [0]*(2**(max_layer+1)-1)
        for i in in1:
            lst[i[1]-1] = i[0]
        queue = [1]
        visited = []
        while queue:
            data = queue.pop(0)
            if data-1 < len(lst):
                if lst[data-1]:
                    visited.append(str(lst[data-1]))
                    queue.append(2*data)
                    queue.append(2*data+1)
        if len(visited) != len(in1):
            print("not complete")
        else:
            print(" ".join(visited))    
    except:
        break

"""
(11,LL) (7,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(3,L) (4,R) ()
(11,LL) (7,LLL) (2,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(5,) (3,) (4,R) ()
(5,) (3,LL) ()
(5,) ()
"""