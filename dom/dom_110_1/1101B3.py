
for i in range(int(input())):
    y = int(input())

    print("Case %d: "%(i+1),end="")
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