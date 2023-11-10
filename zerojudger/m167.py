for _ in range(int(input())):
    l1,l2 = map(list,input().split())

    if len(l1)==len(l2):
        while l1:
            a = l1.pop(0)
            for i in range(len(l2)):
                if a==l2[i]:
                    del l2[i]
                    break
        if l2:
            print(False)
        else:
            print(True)

    else:
        print(False)


"""
YPBKVHERBR VTGFZF

CNPLMFUH 
MHLCNFUP
"""