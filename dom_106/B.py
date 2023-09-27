dit = {
    "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
}
def f(x):
    if in1[x] > in1[x-1]:
        in1[x] = in1[x]-in1[x-1]
        del in1[x-1]
    if x < len(in1)-1:
        f(x+1)

for _ in range(int(input())):
    in1 = input()
    in1 = [ dit[i] for i in in1 ] 
    if len(in1) > 1:
        f(1)
        print(sum(in1))
    else:
        print(in1[0])

"""
8
IX
VI 
XI
XVII
CCLXVIII
MMMCC
DCCVII
MMCDLXIX 
"""