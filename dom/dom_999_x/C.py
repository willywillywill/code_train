in1 = list(map(int,input().split()))
lst = []
for i in range(in1[0]):
    lst += list(map(int,input().split()))
print(max(lst))
