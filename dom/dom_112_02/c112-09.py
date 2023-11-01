in1 = int(input())
in2 = int(input())
out = []
for i in range(in1,in2+1):
    k = 1
    for j in str(i):
        if int(j)==0:
            k=0
            break
        if i%int(j) != 0:
            k=0
            break
    if k:
        out.append(i)
print(len(out))
