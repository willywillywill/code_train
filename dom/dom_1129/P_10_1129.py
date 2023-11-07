
while 1:
    try:
        s = list(map(int, input().split(",")))
        num = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j] and i!=j and i<j:
                    num+=1
        print(num)
    except:
        break

"""
1,2,3,1,1,3

"""