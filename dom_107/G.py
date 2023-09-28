
node = {}
lst = []
in1 = list(map(int, "1,2,3,4,5".split(",")))

for i in range(len(in1)):
    if 2*i+1 < len(in1):
        if in1[i] not in node:
            node[in1[i]] = [in1[2*i+1]]
        else:
            node[in1[i]].append(in1[2*i+1])
    if 2*i+2 < len(in1):
        if in1[i] not in node:
            node[in1[i]] = [in1[2*i+2]]
        else:
            node[in1[i]].append(in1[2*i+2])

print(node)


"""
5
[6,5,7]
[1,2,3,4,5]
[1,2,3,4,6,null,7]
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,null,null,null,null,null,null,15]
"""