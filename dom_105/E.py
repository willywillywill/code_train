H_tree = {}
B_tree = {}

tree = {}

in1 = list(map(int, "4,8,6,1,10,16,5,14,13".split(",")))

for i in range(len(in1)):
    if i:
        tree[i] = [in1[2*i],in1[2*i+1]]
    else:
        tree[0] = [in1[1],in1[2]]
print(tree)