while 1:
    try:
        n = int(input())
        if not n:
            break
        while 1:
            stack1 = list(range(1,n+1))
            in1 = list(map(int,input().split()))
            if sum(in1)==0:
                break
            stack2 = []
            while stack1:
                stack2.append(stack1.pop(0))
                while stack2:
                    if stack2[-1] == in1[0]:
                        stack2.pop(-1)
                        in1.pop(0)
                    else:
                        break
            if not in1:
                print("Yes")
            else:
                print("No")
        print()
    except:
        break

    

