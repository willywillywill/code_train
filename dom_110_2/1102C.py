
while 1:
    try:
        s = input()
        a = [ "+" if i%2==0 else "-" for i in range(len(s)-1) ]
        ans = []
        for i in range(len(s)-1):
            ans.append(s[i])
            ans.append(a[i])
        ans.append(s[-1])
        print(eval("".join(ans)))
    except:
        break