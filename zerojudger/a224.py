# aba -> b
while 1:
    try:
        n = input().lower()
        s = set(n)
        a = 0
        t = "abcdefghijklmnopqrstuvwxyz"
        for i in s:
            if i in t:
                c = n.count(i)
                if c%2 != 0:
                    a = a+1
        if a <= 1:
            print("yes !")
        else:
            print("no...")
    except:
        break