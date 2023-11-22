
lst = []
for _ in range(int(input())):
    lst.append(int(input()))
m = int(input())
lst.sort()
for i in lst:
    print(i)
if m in lst:
    print("Yes")
else:
    print("No")