
name = []
while 1:
    try:
        s = input()
        if s in name:
            print("YES")
        else:
            name.append(s)
            print("NO")
    except:
        break