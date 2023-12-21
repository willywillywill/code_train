arr = []
for i in range(3):
    arr.append(list(map(int,input().split())))
a = arr[0][1]+arr[0][2]
b = arr[1][0]+arr[0][2]
c = arr[2][0]+arr[0][1]
total = (a+b+c)//2
arr[0][0] = total-a
arr[1][1] = total-b
arr[2][2] = total-c
print()
for i in arr:
    print(*i)


"""
0 1 1
1 0 1
1 1 0
"""