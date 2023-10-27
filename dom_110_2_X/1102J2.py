input()
for i in list(map(int,input().split())):
    while i%2==0: i/=2
    while i%3==0: i/=3
    while i%5==0: i/=5

    print(i==1)



"""
4
1024 235 450 245
"""