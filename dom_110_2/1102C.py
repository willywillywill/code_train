
while 1:
    try:
<<<<<<< HEAD
        s = list(input())
        ans = [ "+" if i%2==0 else "-" for i in range(len(s)-1) ]
        out = [ str(s[i])+str(ans[i]) for i in range(len(ans)) ]
        print(eval("".join(out)+s[-1]))
=======
        s = input()
        a = [ "+" if i%2==0 else "-" for i in range(len(s)-1) ]
        ans = []
        for i in range(len(s)-1):
            ans.append(s[i])
            ans.append(a[i])
        ans.append(s[-1])
        print(eval("".join(ans)))
>>>>>>> 2891908291cc719ddac87077dbe619babe8d4937
    except:
        break