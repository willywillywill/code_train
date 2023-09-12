
lst = [1]

for i in range(1,11):
    lst.append(lst[i-1]*i)

while 1:
    try:
        s = int(input())
        if s > len(lst)-1:
            for i in range(len(lst), s+1):
                if lst[i-1]*i > 6227020800:
                    print("Overflow!")
                    break
                else:
                    lst.append(lst[i-1]*i)
        else:
            if lst[s] > 6227020800:
                print("Overflow!")
            elif lst[s] < 10000:
                print("Underflow!")
            else:
                print(lst[s])
    except:
        break


