s,k = 0,1
for i in range(20,41,3):
    for j in range(2,11):
        if i/j == i//j:
            print(i,j)
            s += j*k
    k *= -1
print(s)
