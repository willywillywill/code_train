for _ in range(int(input())):
    lst = list(map(str, input().split()))
    check_lst = [ int("".join(lst[i:i+2]),16) for i in range(0,len(lst),2) ]
    check_sum = hex(sum(check_lst))[2:][::-1]
    check_lst = [ check_sum[i:i+4][::-1] for i in range(0,len(check_sum),4) ]
    s = hex(int(check_lst[0],16)+int(check_lst[1],16))
    s = bin(int(s,16))[2:]
    if len(s)%4 != 0:
        s = "0"*(((len(s)//4)*4+4)-len(s))+s
    s = int("".join([ str(int(not int(i))) for i in s ]),2)
    s = hex(s)[2:]
    if s != 4:
        s = "0"*(4-len(s))+s
    print(s)


"""
5
45 00 00 30 cc 61 40 00 40 06 00 00 0a 05 04 6b 0a 08 09 ed
45 00 00 73 00 00 40 00 40 11 b8 61 c0 a8 00 01 c0 a8 00 c7
45 00 00 47 73 88 40 00 40 06 00 00 83 9f 0e 85 83 9f 0e a1
45 00 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1
45 00 05 14 42 a2 21 40 80 01 00 00 c0 a8 00 03 c0 a8 00 01

"""