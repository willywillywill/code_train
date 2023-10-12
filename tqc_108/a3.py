k = []
in1 = int(input())
in2 = int(input())
for i in range(in1,in2):
    if (i%4==0 or i%6==0) and i%12!=0:
        k.append(i)
for i in range(len(k)):
    if i%10==0 and i:
        print()
    print("%-4d"%(k[i]), end="")
print()
print(len(k))
print(sum(k))