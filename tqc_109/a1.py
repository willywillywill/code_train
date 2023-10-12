# 2:19
lst = []
for i in range(4):
    lst.append(int(input()))
print(*lst)
print("Sum = %.2f"%(sum(lst)))
print("Average = %.2f"%(sum(lst)/len(lst)))