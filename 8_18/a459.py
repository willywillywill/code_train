b, s = list(map(str, input().split()))
b = int(b)
num=0
for i in s:
    num += int(i)**len(s)

if num == int(s, b):
    print("YES")
else:
    print("NO")