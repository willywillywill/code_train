for _ in range(int(input())):
    in1 = input()
    out = 0
    b = 0
    for i in in1:
        if i == "O":
            b+=1
            out += b
        else:
            b=0
    print(out)


"""
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOX

"""