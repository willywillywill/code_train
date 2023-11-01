# 3:50

in1 = int(input())
in2 = int(input())

lst = []
for i in range(in1,in2+1):
    if (i%4==0 or i%6==0) and (i%12!=0):
        lst.append(i)

k = 0
for i in range(len(lst)):
    if i%10==0 and i:
        print()
        k=0
    print("%-4d"%(lst[i]),end="")
    k=1
if k:
    print()
print(len(lst))
print(sum(lst))