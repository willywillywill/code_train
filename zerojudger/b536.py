
for _ in range(int(input())):
    in1 = list(input().replace("-",""))
    chick = in1[-1]
    lst = list(map(int,in1[:-1]))

    if len(lst)==9:
        lst = [ (10-i)*lst[i] for i in range(len(lst)) ]
        s = sum(lst)%11
        n = 11-s
        if n==10:
            n = "X"
        else:
            n = str(n)
        if n==11:
            n = "0"
        else:
            n = str(n)

        if n==chick:
            print("T")
        else:
            print("F")
    else:
        lst = [ (3 if i%2 else 1) *lst[i] for i in range(len(lst)) ]
        s = sum(lst)%10
        n = 10 - s
        if n==10:
            n = "0"
        else:
            n = str(n)
        if n==chick:
            print("T")
        else:
            print("F")