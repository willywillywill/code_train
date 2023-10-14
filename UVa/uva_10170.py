s,d = list(map(int, input().split()))

lst = []

while len(lst) < d:
    for i in range(s):
        lst.append(s)
        if len(lst) >= d:
            break
    s+=1
print(lst)
print(lst[-1])