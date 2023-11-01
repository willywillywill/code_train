
while 1:
    y = int(input())
    if not y:
        break
    if y%4==0:
        if y%100==0:
            if y%400==0:
                print("a leap year")
            else:
                print("a normal year")
        else:
            print("a leap year")
    else:
        print("a normal year")