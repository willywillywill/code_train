for _ in range(int(input())):
    in1 = "$"+input()
    n = [0]*len(in1)
    for i in range(1,len(in1)):
        if in1[i]=="O":
            n[i] += n[i-1]+1
    print(sum(n))