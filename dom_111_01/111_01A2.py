in1 = int(input())
in2 = int(input())
in1,in2 = min(in1,in2),max(in1,in2)
for i in range(in1+1, in2):
    if i%5==2 or i%5==3:
        print(i)