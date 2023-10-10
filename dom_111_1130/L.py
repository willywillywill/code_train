

num=0
for i in range(1,int(input())+1):
    b = str(bin(i))
    for j in b:
        if j == "1":
            num+=1
print(num)