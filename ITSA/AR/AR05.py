n = int(input())
lst = list(map(int,input().split()))
arr = [0]*25

for i in range(0,len(lst),2):
    start = lst[i]
    end = lst[i+1]
    
    for j in range(start, end):
        arr[j] += 1
print(max(arr))
"""
3
1 6 3 12 6 18
"""