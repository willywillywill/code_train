input()
lst = list(map(int,input().split()))
for _ in range(int(input())):
    print(lst.count(int(input())))