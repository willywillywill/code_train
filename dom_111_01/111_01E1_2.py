def f_s(s):
    global max_layer,val,idx
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
    #val.append(s[0])
    #idx.append(k)
    return s

def dfs(i):
    if i in idx:
        visited[i-1]=str(val[idx.index(i)])
        dfs(2*i)
        dfs(2*i+1)

while 1:
    try:
        max_layer = 0
        val = []
        idx = []
        list(map(f_s, input()[:-2].split()))
        visited = [0]*(2**(max_layer+1)-1)
        dfs(1)
        visited = [ i for i in visited if i ]
        if len(visited) == len(val):
            print(" ".join(visited))
        else:
            print("not complete")
    except:
        break

"""
(11,LL) (7,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(3,L) (4,R) ()
(11,LL) (7,LLL) (2,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()

(5,) (3,RR) (4,R) ()
"""