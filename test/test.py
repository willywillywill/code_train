arr = [
    [5,1,3],
    [2,0,2],
    [3,1,5]
]
for i in range(len(arr)):
    for j in range(len(arr)):
        arr[i][j] == arr[len(arr)-1-i][len(arr)-1-j]
