
while 1:
    try:
        lst = []
        for i in range(int(input())):
            lst.append(int(input()))
        lst.sort()
        for i in lst:
            print(i)
    except:
        break