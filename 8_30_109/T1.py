
num = []
for i in range(4):
    num.append(int(input()))
for i in num:
    print(i,end=" ")
print()
print("Sum =",sum(num))
print("Average = %.2f"%(sum(num)/4))
