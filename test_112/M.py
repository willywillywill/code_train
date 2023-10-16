def f(i,l):
    k = str(sum([ int(j)**2 for j in i ]))
    if k in l:
        return l
    l.append(k)
    return f(k,l.copy())

for i in range(int(input())):
    n = input()
    l = f(n,[])
    if l[-1]=="1":
        print("Case #%d:"%(i+1),n,"is a Happy number.")
    else:
        print("Case #%d:"%(i+1),n,"is an Unhappy number.")