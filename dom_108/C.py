
for _ in range(int(input())):
    in1 = list(map(int, input().split()))
    lst = list(map(str, range(in1[0],in1[1]+1)))
    lst = [ i for i in lst if str(in1[2]) in i ]
    print(len(lst))

"""
3
3 17 3
0 20 0
0 150 17
"""