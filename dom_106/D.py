import itertools

for _ in range(int(input())):
    in1 = list(map(str, input().split(",")))
    lst = list(itertools.permutations(in1[0],len(in1[0])))
    r1,r2 = lst[int(in1[1])-1],lst[int(in1[2])-1]
    A = 0
    B = 0
    for i in range(len(r1)):
        for j in range(len(r2)):
            if r1[i] == r2[j]:
                if i==j:
                    A+=1
                else:
                    B+=1
    print(str(A)+"A"+str(B)+"B")

"""
3
12,1,2
123,1,2
123,2,5

4
1234,15,9
1234,3,4
1234,1,24
1234,1,1 
"""