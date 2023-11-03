for _ in range(int(input())):
    ans = [ i for i in input() if i.isdigit() or i in list(" +  -  *  /  % ".split()) ]
    print(eval("".join(ans)))