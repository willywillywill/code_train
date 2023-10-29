for _ in range(int(input())):
    lst = input().split()
    check_lst = [ int("".join(lst[i:i+2]),16) for i in range(0,len(lst),2) ]
    check_sum = hex(sum(check_lst))[2:]
    ans = int(check_sum[:len(check_sum)-4],16)+int(check_sum[len(check_sum)-4:],16)
    ans = bin(ans)[2:].rjust(16,"0")
    opt = "".join([ "1" if i=="0" else "0" for i in ans ])
    print(hex(int(opt,2))[2:].rjust(4,"0"))

"""
5
45 00 00 30 cc 61 40 00 40 06 00 00 0a 05 04 6b 0a 08 09 ed
45 00 00 73 00 00 40 00 40 11 b8 61 c0 a8 00 01 c0 a8 00 c7
45 00 00 47 73 88 40 00 40 06 00 00 83 9f 0e 85 83 9f 0e a1
45 00 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1
45 00 05 14 42 a2 21 40 80 01 00 00 c0 a8 00 03 c0 a8 00 01

"""