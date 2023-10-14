# OK

def f(s):
    for i in range(len(s)):
        if (s[i]=="*") and (s[i+1]== "*"):
            return True
    return False

while 1:
    try:
        s = input().replace(" ", "*")
        s = list(s)

        cnt = 0
        while f(s):
            i=0
            while i<len(s):
                if (s[i]=="*") and (s[i+1]== "*"):
                    del s[i]
                i+=1
            cnt+=1
        print(cnt)
    except:
        break
