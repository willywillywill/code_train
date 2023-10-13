# 2:19
# 3:32

lst = []
for i in range(4):
    lst.append(eval(input()))
print(*lst)
print("Sun = %.2f"%(sum(lst)))
print("Average = %.2f"%(sum(lst)/len(lst)))