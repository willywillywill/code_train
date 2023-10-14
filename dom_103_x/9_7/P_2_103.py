f = lambda x,y: d1*x+d2*y==t

for _ in range(int(input())):
    num, d1,d2, t = list(map(int, input().split(",")))    

    for i in range(num+1):
        k = num-i
        if f(i,k):
            print(str(i)+","+str(k))
            break