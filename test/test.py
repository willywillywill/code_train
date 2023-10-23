def func(n,m):
    arr = [0]*100
    tail = 0
    for i in range(1,n+1):
        arr[tail] = i
        tail=tail+1
    head = -1
    count = 0
    while tail > head+1:
        count += 1
        head += 1
        if count==m:
            arr[tail] = arr[head]
            count = 0
            tail+=1
    print(arr)
    return arr[head]
print(func(30,4))