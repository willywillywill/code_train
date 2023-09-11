# ! KMP 

"""
s = input()
while s != ".":
    next = [0]
    j = 0
    i = 1
    n = 0
    while i < len(s):
        if s[j] == s[i]:
            j += 1
            next.append(j)
            i+=1
        else:
            j = next[j - 1]
            if j == 0:
                next.append(0)
                n = len(next)
                i+=1

    if n:
        print( 1 if (n > int(len(s)/2)) or len(s)%n or (len(s) == 1) else int(len(s)/n))
    else:
        print(len(next))

    s = input()
"""

    


while 1:
    s = input()
    if s == ".":
        break

    ks = s[0]
    e = 0
    for i in range(1, len(s)): # 尋找重復的位置
        if s[i]==ks:
            e = i
            break
    if e:
        ks = s[:e]
        num = 0
        for i in range(len(s)-(len(ks)-(len(ks)-1))+1): # 尋找重復字串
            k = s[i:i+len(ks)]
            if ks == k: # 找到重複字串
                num+=1

        print(num)
    else:
        print(1)