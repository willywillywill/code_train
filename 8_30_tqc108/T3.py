num = 0
lis = []
for i in range(int(input()), int(input())):
    if not(i%4==0 ^ i%6==0):
        if i%4==0 or i%6==0:
            print("%-4d"%(i), end="")       
            num+=1
            lis.append(i)
            if num==10:
                print()
print()
print(len(lis))
print(sum(lis))