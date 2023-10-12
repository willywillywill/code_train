def f_s(s):
    global max_layer
    s = s.replace("(","")
    s = s.replace(")","")
    s = s.split(",")
    max_layer = max(max_layer, len(s[1]))
    return s
def dfs(i):
    if i-1 > len(visited)-1:
        return
    if ans[i-1]:
        visited[i-1]=1
        dfs(2*i)
        dfs(2*i+1)
    else:
        return
while 1:
    try:
        max_layer = 0
        in1 = list(map(f_s, "(5,) (4,R) (3,LL) ()"[:-2].split()))
        ans = [0]*(2**(max_layer+1)-1)

        for i in in1:
            k = 1
            for j in i[1]:
                if j=="L":
                    k = k*2
                else:
                    k = k*2+1
            if ans[k-1]:
                print("not complete")
                break
            ans[k-1] = i[0]
        else:
            visited = [0]*(2**(max_layer+1)-1)
            if ans[0]:
                dfs(1)
                t_ans = [ int(bool(i)) for i in ans ]
                if t_ans==visited:
                    ans = [ i for i in ans if i ]
                    print( " ".join(ans) )
                else:
                    print("not complete")
            else:
                print("not complete")
    except:
        break