
def f_s(s:str):
    global stop_input,end
    s = s.replace("(","")
    s = s.replace(")","")
    s = s.split(",")
    if s==[""]:
        stop_input=1
    else:
        n = 1
        for i in s[1]:
            n = n*2 if i=="L" else n*2+1
        if n in tree:
            end = 1

        tree[n] = int(s[0])
while 1:
    try:
        stop_input = 0
        end = 0
        tree = {}
        while 1:
            in1 = list(map(f_s, input().split()))
            if stop_input:
                break

        if end or ( 1 not in tree):
            print("not complete")
            continue

        queue = [1]
        visited = tree.copy()
        for i in visited:
            visited[i] = 0
        while queue:
            idx = queue.pop(0)
            if idx in tree:
                if tree[idx]:
                    visited[idx] = tree[idx]
                    queue.append(idx*2)
                    queue.append(idx*2+1)
        if visited == tree:
            out = [ visited[i] for i in sorted(list(visited.keys()))]
            print(*out)
        else:
            print("not complete")
    except:
        break
