for _ in range(int(input())):
    y = int(input())
    print("Case %d: "%(_+1),end="")
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
