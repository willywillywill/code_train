arr = [0]*100
tail = 0
for i in range(1,30+1):
    arr[tail] = i
    tail += 1
head = -1
count = 0
while tail>head+1:
    count += 1
    head += 1
    if count==4:
        arr[tail] = arr[head]
        count = 0
        tail += 1
print(arr)