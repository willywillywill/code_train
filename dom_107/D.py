import itertools

for _ in range(int(input())):
    in1 = list(map(int,input().split(",")))
    k = in1[-1]
    in1 = in1[1:in1[0]+1]
    lst = list(itertools.permutations(in1, len(in1)))
    lst.sort()
    for i in lst[k-1]:
        print(i,end="")
    print()


"""
4
2,0,2,1
3,0,3,9,1
3,0,3,9,6
4,4,5,6,7,24
"""