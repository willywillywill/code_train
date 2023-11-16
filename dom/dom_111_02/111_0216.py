lst = list(map(int,input().split()))

for i in set(lst):
    if lst.count(i) == len(lst)//2:
        print(i)
        break