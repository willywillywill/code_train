lst1 = [1,2,3,4,5,6,7,8,9,0]

lst2 = []

for i in lst1:
    if i%3:
        continue

    for j in range(10):
        lst2.append(j-i)
        print(j,i)
        if j%2==1:
            break
print(lst2)