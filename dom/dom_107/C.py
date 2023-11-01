
for _ in range(int(input())):
    n = input()
    in1 = list(n)
    for _ in range(int(n)):
        in1 = [ int(i)**2 for i in in1 ]
        in1 = [str(sum(in1))]
        in1 = [[ j for j in i ] for i in in1 ]
        in1 = [ j for i in in1 for j in i ]
        if in1[0]=="1" and len(in1)==1:
            print("T")
            break
    else:
        print("F")

"""
8
68
49
14
65
213
9437
100000
99999
"""