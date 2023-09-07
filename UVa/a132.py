while 1:
    num = int(input())
    if num==0:
        break
    b = bin(num)
    c=0
    for i in b:
        if i=="1":
            c+=1
    print("The parity of %s is %s (mod 2)."%(b[2:len(b)], c))
