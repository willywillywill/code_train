n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

print(arr[n//4],arr[n//2-1] if n%2==0 else arr[n//2],arr[(3*n)//4])


"""
11
6
47
49
15
42
41
7
39
43
40
36

6
15
7
36
41
40
39

"""