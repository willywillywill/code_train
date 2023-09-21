in1 = list(map(int,input().split()))
in1 = [ (i%14)+(i//14) for i in in1 ]
same_dit = {
    2:0,
    3:0,
    4:0
    }
print(in1)
while in1:
    k1 = in1.pop(0)
    k1_n = 1
    while (k1 in in1):
        del in1[in1.index(k1)]
        k1_n+=1
    if k1_n in same_dit:
        same_dit[k1_n]+=1
print(same_dit)

"""
3 44 4 6 7 5 
19 12 1 32 45 25
"""