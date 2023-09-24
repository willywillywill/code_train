
for _ in range(int(input())):
    in1 = list(map(int, input().split(",")))
    k1=1  # 1 -> yes 
    k2=1 
    k3=1
    for i in range(len(in1)):  
        if 2*i+1 < len(in1):   # Max Heap Tree
            if in1[i] < in1[2*i+1]:
                k1=0
        if 2*i+2 < len(in1):
            if in1[i] < in1[2*i+2]:
                k1=0

        if 2*i+1 < len(in1):   # Min Heap Tree
            if in1[i] > in1[2*i+1]:
                k2=0
        if 2*i+2 < len(in1):
            if in1[i] > in1[2*i+2]:
                k2=0
        
        if 2*i+1 < len(in1):   # BST
            if in1[i] < in1[2*i+1]:
                k3=0
        if 2*i+2 < len(in1):
            if in1[i] > in1[2*i+2]:
                k3=0
        
    if k1 or k2:
        print("H")
    elif k3:
        print("B")
    else:
        print("F")

"""
4
16,14,13,4,8,6,5,10,1
16,14,10,13,4,6,5,1,8
7,4,12,1,5,8,10
9,6,12,2,8,11,15,1,3,7 

"""
