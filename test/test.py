
n = 9
lst = [0]*n
left = []
right = []
for i in range(n,0,-1):
    if i%2==0:
        left.append(i)
    else:
        right.insert(0,i)
print(left+right)