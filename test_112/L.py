def f(i):
    if len(i)==1:
        return 2
    k = str(sum([ int(j) for j in i ]))
    return f(k)

while 1:
    n = input()
    if n=="0":
        break
    print(f(n))
