"""
5
1234567891234563
4013735633800642
5181271099000017
5241150318192904
5241150313182900 

3
1234567891234561
4013735633800643
5181271099000014
"""
def f(num):
    i,num = num
    i = 2 if i % 2 == 0 else 1
    num = str(int(num) * i)
    num = int(num[0])+int(num[1]) if len(num) > 1 else int(num)
    return num

for _ in  range(int(input())):
    in1 = list(map(f, enumerate(input().strip())))
    print( "F" if sum(in1)%10 else "T")