date = []
t = "Saturday Sunday Monday Tuesday Wednesday Thursday Friday".split()

j = 0
for i in range(365):
    date.append(t[j])
    j+=1
    j %= 7

for _ in range(int(input())):
    a1,a2 = list(map(int,input().split()))
    n = 0
    for i in range(1,a1):
        if i in [1,3,5,7,8,10,12]:
            n+=31
        elif i==2:
            n+=28
        else:
            n+=30
    n+=a2
    print(date[n-1])