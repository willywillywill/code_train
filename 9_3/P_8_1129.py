while 1:
    try:
        s = list(map(int, input().replace(" ",",").split(",")))
        num = s.pop(-1)
        k = []
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i]+s[j]==num and i!=j and not k:
                    k = [str(i),str(j)]

        print(",".join(k))
    except:
        break



"""
2,7,11,15 9

"""