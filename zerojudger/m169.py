def main(n):
    lst = []
    for _ in range(n):
        lst.append(input())

    T = True

    out = [lst.pop(0)]
    while lst:
        for j in range(len(lst)):
            if out[-1][-1] == lst[j][0]:
                out.append(lst.pop(j))
                break
        else:
            T = False
            break

    T = out[0][0]==out[-1][-1]

    if T:
        print("OK")
    else:
        print("NG")

while 1:
    n = int(input())
    if n==0:
        break
    main(n)