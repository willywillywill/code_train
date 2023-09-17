# !!!

def f(n):
    global lst
    if n == 1:
        return
    if len(lst)==2:
        lst = lst[::-1]+lst
    else:
        lst = lst+lst[::-1]

    for i in range(len(lst)):
        if i < len(lst)/2:
            lst[i] = "0" + lst[i]
        else:
            lst[i] = "1" + lst[i]
    f(n-1)

n = int(input())
lst = ["1","0"]

f(n)
for i in lst:
    print(i)


