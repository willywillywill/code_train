
while 1:
    try:
        lst = input().replace("#","").split()
        if "~" in lst:
            break
        f = 0
        ans = []
        for i in range(len(lst)):
            if len(lst[i])==1:
                f = 1
            elif len(lst[i])==2:
                f = 0
            else:
                for j in range(len(lst[i])-2):
                    ans.append(str(f))
        ans = int("".join(ans),2)
        print(ans)
    except:
        break
"""
0 0000 00 000 0 0000
0 000
"""