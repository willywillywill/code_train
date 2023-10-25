
while 1:
    try:
        s = list(input())
        ans = [ "+" if i%2==0 else "-" for i in range(len(s)-1) ]
        out = [ str(s[i])+str(ans[i]) for i in range(len(ans)) ]
        print(eval("".join(out)+s[-1]))
    except:
        break