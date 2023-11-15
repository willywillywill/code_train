n,d = map(int,input().split())
lst = list(map(int,input().split()))

val = 0
k = 0
b = lst.pop(0)
for i in lst:
    if b == None:
        if i <= k-d:
            b = i
    elif i >= b+d:
        val += i-b
        b = None
        k = i
print(val)