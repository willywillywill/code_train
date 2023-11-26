d = {}
b = {}
ans = []
while 1:
    s = input().split()
    if s[0]=="clear":
        break
    elif s[0]=="def":
        d[s[1]] = s[2]
        b[s[2]] = s[1]
    else:
        a = s[1:].copy()
        s = s[1:-1]
        f = False
        
        for i in range(0,len(s),2):
            if s[i] in d:
                s[i] = d[s[i]]
            else:
                f = True
        if f:
            a.append("unknown")
        else:
            l = str(eval("".join(s)))
            if l not in b:
                a.append("unknown")
            else:
                a.append(b[l])
        ans.append(" ".join(a))
for i in ans:
    print(i)


"""
def foo 3
calc foo + bar =
def bar 7
def programming 10
calc foo + bar =
def is 4
def fun 8
calc programming - is + fun =
def fun 1
calc programming - is + fun =
clear
"""