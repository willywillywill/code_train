in1 = input()
k = 0
ans = 0
for i in range(1,len(in1)):
    if in1[i]==in1[i-1]:
        k += 1
    else:
        k = 0
    if k >= 2:
        ans += 1
print(ans)