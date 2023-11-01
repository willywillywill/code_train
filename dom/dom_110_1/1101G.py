n = int(input())

lst = ["0","1"]

for i in range(n-1):
    lst = lst+lst[::-1]
    a1 = [ "0"+i for i in lst[:len(lst)//2] ]
    a2 = [ "1"+i for i in lst[len(lst)//2:] ]
    lst = a1+a2

for i in lst:
    print("".join(i))