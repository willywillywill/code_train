in1 = list(input())
in2 = list(input())

while in2:
    f = in2.pop(0)
    if f=="+":
        in1 = list(str(int("".join(in1))+1))
        a = in1.pop(-1)
        in1 = [a]+in1
    elif f=="-":
        in1 = list(str(int("".join(in1))-1))
        a = in1.pop(0)
        in1 = in1+[a]
    in1 = list(str(int("".join(in1))))

print("".join(in1))    
