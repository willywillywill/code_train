while 1:
    y = int(input())
    if not y:
        break

    if y%4:
        print("a normal year")
    else:
        if y%100:
            print("a leap year")
        else:
            if y%400:
                print("a normal year")
            else:
                print("a leap year")
