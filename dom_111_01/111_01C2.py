
for _ in range(int(input())):
    in1 = int(input())
    num = list(map(str,range(1,in1+1)))
    dit = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

    for i in num:
        for j in i:
            dit[int(j)]+=1
    for i in range(10):
        print(dit[i],end=" ")
    print()