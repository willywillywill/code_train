
for _ in range(int(input())):
    in1 = input().replace("[","").replace("]","").split(",")
    if in1==[""]:
        print([])
        continue
    
    in1 = [0]+list(map(int,in1))
    ans = []
    que = [1]
    while que:
        idx = que.pop(0)
        ans.append(in1[idx])

        if idx*2+1 < len(in1):
            que.append(idx*2+1)
        if idx*2 < len(in1):
            que.append(idx*2)
    print(str(ans).replace(" ",""))
"""
3
[4,2,7,1,3,6,9]
[2,1,3]
[]


"""