in1 = input().split()
for i in range(int(input())):
    in2 = input().split()
    vis = [0]*len(in1)
    for i in range(len(vis)):
        if in1[i]==in2[i]:
            vis[i] = "A"
        else:
            for j in range(len(vis)):
                if i!=j and in1[i]==in2[j] and not vis[j]:
                    vis[j] = "B"
                    break
            else:
                if not vis:
                    vis[i] = ""
    print("%dA%dB"%(vis.count("A"),vis.count("B")))