           

n = int(input())
num = []
for i in range(2,n):
    lst = []
    for j in range(2,i):
        if i%j == 0:
            lst.append(i)
    if not lst:
        k = list(str(i))
        if k == k[::-1]:
            print("%-4s"%("".join(k)),end="")

print(sum(num))